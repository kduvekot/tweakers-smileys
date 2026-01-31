#!/bin/bash
#
# Secure GitHub CLI Installation Script with Version Checking
# Alternative to gh-setup-hooks with enhanced security
#
# This script:
# - Downloads gh CLI from official GitHub releases
# - Performs BLOCKING checksum verification
# - Uses secure download methods (HTTPS, TLS 1.2+)
# - Checks for newer versions available
# - Cleans up temporary files
# - Logs all actions for audit trail
#

set -e  # Exit on any error
set -u  # Exit on undefined variable
set -o pipefail  # Exit on pipe failures

# Configuration
VERSION="${GH_SETUP_VERSION:-2.83.2}"
ARCH="amd64"
INSTALL_DIR="${HOME}/.local/bin"
BASE_URL="https://github.com/cli/cli/releases/download/v${VERSION}"
TARBALL="gh_${VERSION}_linux_${ARCH}.tar.gz"
CHECKSUMS_FILE="gh_${VERSION}_checksums.txt"

# Version check configuration
CHECK_FOR_UPDATES="${GH_CHECK_UPDATES:-true}"  # Set to "false" to disable
VERSION_CHECK_TIMEOUT=2  # seconds (fast fail if API is slow)

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Logging functions
log() {
    echo -e "${GREEN}[gh-install]${NC} $*" >&2
}

error() {
    echo -e "${RED}[gh-install ERROR]${NC} $*" >&2
}

warn() {
    echo -e "${YELLOW}[gh-install WARN]${NC} $*" >&2
}

info() {
    echo -e "${BLUE}[gh-install INFO]${NC} $*" >&2
}

# Check for newer version available (non-blocking)
check_for_updates() {
    if [ "$CHECK_FOR_UPDATES" != "true" ]; then
        return 0
    fi

    info "Checking for updates..."

    # Use timeout to prevent hanging (non-blocking)
    local latest_version=""
    local api_url="https://api.github.com/repos/cli/cli/releases/latest"

    # Try to get latest version with timeout
    if latest_version=$(curl -fsSL --max-time "$VERSION_CHECK_TIMEOUT" "$api_url" 2>/dev/null | grep -o '"tag_name": *"[^"]*"' | cut -d'"' -f4 | tr -d 'v'); then

        if [ -n "$latest_version" ]; then
            # Compare versions (simple string comparison works for x.y.z format)
            if [ "$latest_version" != "$VERSION" ]; then
                echo ""
                warn "════════════════════════════════════════════════════════════"
                warn "  A newer version of GitHub CLI is available!"
                warn "  Current/Target: v${VERSION}"
                warn "  Latest:         v${latest_version}"
                warn ""
                warn "  Release notes:"
                warn "  https://github.com/cli/cli/releases/tag/v${latest_version}"
                warn ""
                warn "  To update, change VERSION in .claude/install-gh.sh"
                warn "  Or set: export GH_SETUP_VERSION=${latest_version}"
                warn "════════════════════════════════════════════════════════════"
                echo ""
            else
                info "✓ You are using the latest version (v${VERSION})"
            fi
        fi
    else
        # API check failed (timeout, network issue, rate limit, etc.)
        # This is non-blocking - just skip the check
        : # no-op
    fi
}

# Version comparison helper (returns 0 if v1 < v2)
version_lt() {
    [ "$1" != "$2" ] && [ "$(printf '%s\n' "$1" "$2" | sort -V | head -n1)" = "$1" ]
}

# Only run in remote Claude Code environment
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
    log "Not in Claude Code remote environment, skipping installation"
    exit 0
fi

# Check if gh is already installed
if command -v gh &> /dev/null; then
    CURRENT_VERSION=$(gh --version | head -n1 | awk '{print $3}')
    log "GitHub CLI already installed: v${CURRENT_VERSION}"

    if [ "$CURRENT_VERSION" = "$VERSION" ]; then
        log "Version matches target, skipping installation"

        # Still check for updates
        check_for_updates

        exit 0
    else
        warn "Installed version (${CURRENT_VERSION}) differs from target (${VERSION})"
        warn "Proceeding with installation of v${VERSION}"
    fi
fi

# Check for updates before installing
check_for_updates

log "Installing GitHub CLI v${VERSION}..."

# Create temporary directory with secure permissions
TEMP_DIR=$(mktemp -d)
chmod 700 "$TEMP_DIR"
trap "rm -rf $TEMP_DIR" EXIT

cd "$TEMP_DIR"

# Download tarball
log "Downloading from ${BASE_URL}/${TARBALL}..."
if ! curl -fsSL \
    --proto '=https' \
    --tlsv1.2 \
    --max-time 60 \
    --connect-timeout 10 \
    --retry 3 \
    --retry-delay 5 \
    -o "${TARBALL}" \
    "${BASE_URL}/${TARBALL}"; then
    error "Failed to download tarball"
    exit 1
fi

log "Download complete ($(du -h "${TARBALL}" | cut -f1))"

# Download checksums
log "Downloading checksums..."
if ! curl -fsSL \
    --proto '=https' \
    --tlsv1.2 \
    --max-time 30 \
    --connect-timeout 10 \
    --retry 3 \
    --retry-delay 5 \
    -o "${CHECKSUMS_FILE}" \
    "${BASE_URL}/${CHECKSUMS_FILE}"; then
    error "Failed to download checksums"
    exit 1
fi

# Extract the expected checksum for our file
EXPECTED_CHECKSUM=$(grep "${TARBALL}" "${CHECKSUMS_FILE}" | awk '{print $1}')

if [ -z "$EXPECTED_CHECKSUM" ]; then
    error "Could not find checksum for ${TARBALL} in checksums file"
    exit 1
fi

log "Expected SHA256: ${EXPECTED_CHECKSUM}"

# Verify checksum (BLOCKING - will exit on failure)
log "Verifying checksum..."
ACTUAL_CHECKSUM=$(sha256sum "${TARBALL}" | awk '{print $1}')

if [ "$ACTUAL_CHECKSUM" != "$EXPECTED_CHECKSUM" ]; then
    error "CHECKSUM VERIFICATION FAILED!"
    error "Expected: ${EXPECTED_CHECKSUM}"
    error "Got:      ${ACTUAL_CHECKSUM}"
    error "This could indicate:"
    error "  - Corrupted download"
    error "  - Man-in-the-middle attack"
    error "  - Tampered release files"
    error "ABORTING INSTALLATION FOR SECURITY"
    exit 1
fi

log "✓ Checksum verified successfully"

# Extract tarball
log "Extracting archive..."
if ! tar -xzf "${TARBALL}"; then
    error "Failed to extract tarball"
    exit 1
fi

# Verify extracted binary exists
EXTRACTED_DIR="gh_${VERSION}_linux_${ARCH}"
if [ ! -f "${EXTRACTED_DIR}/bin/gh" ]; then
    error "Binary not found in extracted archive"
    exit 1
fi

# Create install directory if it doesn't exist
mkdir -p "$INSTALL_DIR"

# Install binary
log "Installing to ${INSTALL_DIR}/gh..."
if ! mv "${EXTRACTED_DIR}/bin/gh" "${INSTALL_DIR}/gh"; then
    error "Failed to move binary to install directory"
    exit 1
fi

# Set executable permissions
chmod 755 "${INSTALL_DIR}/gh"

# Update PATH if CLAUDE_ENV_FILE is set
if [ -n "${CLAUDE_ENV_FILE:-}" ]; then
    log "Updating PATH in ${CLAUDE_ENV_FILE}..."
    if ! grep -q "export PATH=\"${INSTALL_DIR}:\$PATH\"" "${CLAUDE_ENV_FILE}" 2>/dev/null; then
        echo "export PATH=\"${INSTALL_DIR}:\$PATH\"" >> "${CLAUDE_ENV_FILE}"
        log "✓ PATH updated"
    else
        log "PATH already configured"
    fi
fi

# Verify installation
if ! "${INSTALL_DIR}/gh" --version &> /dev/null; then
    error "Installation verification failed - binary not working"
    exit 1
fi

INSTALLED_VERSION=$("${INSTALL_DIR}/gh" --version | head -n1 | awk '{print $3}')
log "✓ Successfully installed GitHub CLI v${INSTALLED_VERSION}"

# Security notice
log ""
log "Security notes:"
log "  - Downloaded from: ${BASE_URL}"
log "  - SHA256 verified: ${EXPECTED_CHECKSUM}"
log "  - Installed to: ${INSTALL_DIR}/gh"
log "  - Installation method: Secure script with version checking"
log ""
log "GitHub CLI is ready to use!"

exit 0
