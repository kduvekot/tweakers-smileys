# gh-setup-hooks Security Research Report

## Date: 2026-01-31
## Repository: tweakers-smileys
## Package: gh-setup-hooks v2.0.0

---

## Executive Summary

The `gh-setup-hooks` package is executed automatically via a SessionStart hook to install GitHub CLI in Claude Code on the Web. While the package uses several security best practices, there are **multiple security risks** that should be addressed.

**Risk Level:** 🟡 **MEDIUM** - The package itself is relatively safe, but the execution model and configuration have several vulnerabilities.

---

## What is gh-setup-hooks?

### Source
- **GitHub Repository:** https://github.com/oikon48/gh-setup-hooks
- **NPM Package:** gh-setup-hooks (v2.0.0)
- **Author:** oikon (oikon48)
- **License:** MIT

### Purpose
Automatically installs GitHub CLI (`gh`) in Claude Code on the Web environments during session initialization.

### How It's Used in This Repository

**Configuration in `.claude/settings.json`:**
```json
{
  "hooks": {
    "SessionStart": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "bun x gh-setup-hooks",
            "timeout": 120
          }
        ]
      }
    ]
  }
}
```

---

## How It Works

### Execution Flow

1. **Environment Detection**
   - Checks for `CLAUDE_CODE_REMOTE=true` environment variable
   - Only runs in remote Claude Code environments (skips local)

2. **Version Check**
   - Runs `gh --version` to check if already installed
   - Skips installation if already present

3. **Download Phase**
   - Downloads from: `https://github.com/cli/cli/releases/download/v{VERSION}/gh_{VERSION}_linux_{ARCH}.tar.gz`
   - Downloads checksums from: `https://github.com/cli/cli/releases/download/v{VERSION}/gh_{VERSION}_checksums.txt`
   - Default version: **2.83.2** (configurable via `GH_SETUP_VERSION`)

4. **Verification Phase**
   - Performs SHA256 checksum verification
   - ⚠️ **CRITICAL:** Verification failure does NOT stop installation

5. **Installation Phase**
   - Extracts binary to `~/.local/bin/gh`
   - Updates PATH via `CLAUDE_ENV_FILE`
   - Cleans up temporary files

---

## Security Analysis

### ✅ Security Strengths

1. **Official Source**
   - Downloads from GitHub's official CLI releases
   - Uses HTTPS (enforces TLS 1.2 minimum)

2. **Checksum Verification**
   - Downloads official SHA256 checksums
   - Verifies binary integrity before installation

3. **Environment Isolation**
   - Only runs in remote environments (not local)
   - Respects `CLAUDE_CODE_REMOTE` flag

4. **Timeout Protection**
   - 120-second timeout prevents hanging sessions
   - Curl has connection timeout (5s) and max time (60s)

5. **Clean Installation**
   - Installs to user directory (`~/.local/bin`)
   - Cleans up temporary files after installation

---

## 🚨 Security Risks & Vulnerabilities

### 1. **CRITICAL: Non-Blocking Checksum Verification**

**Risk Level:** 🔴 **HIGH**

**Issue:**
```javascript
// From source code analysis
// Checksum verification failure does NOT stop installation
```

The script continues installation even if SHA256 verification fails. This means:
- Corrupted downloads will be installed
- Potential MITM attacks could inject malicious binaries
- No guarantee of binary integrity

**Impact:**
- Compromised binary could execute arbitrary code
- Full access to repository and GitHub token
- Potential data exfiltration

**Recommendation:**
```javascript
// Should be:
if (checksumFails) {
  throw new Error("Checksum verification failed - aborting installation");
}
```

---

### 2. **HIGH: No Code Signature Verification**

**Risk Level:** 🔴 **HIGH**

**Issue:**
The script verifies file integrity (checksum) but NOT authenticity (signature).

**What This Means:**
- SHA256 only proves the file hasn't been corrupted
- SHA256 does NOT prove GitHub actually created this file
- An attacker controlling the download source could provide malicious files with matching checksums

**Recommendation:**
- Verify GPG signatures of releases
- Pin specific release hashes (not just version)
- Consider using GitHub's attestation API

---

### 3. **MEDIUM: No Version Pinning**

**Risk Level:** 🟡 **MEDIUM**

**Issue:**
```json
"command": "bun x gh-setup-hooks"
```

This downloads the **latest version** of gh-setup-hooks on every session start.

**Risks:**
- Package could be updated with malicious code
- No review process for updates
- Automatic execution of untrusted code
- Supply chain attack vector

**Recommendation:**
```json
"command": "bun x gh-setup-hooks@2.0.0"
```

Pin to a specific, reviewed version.

---

### 4. **MEDIUM: Automatic Code Execution**

**Risk Level:** 🟡 **MEDIUM**

**Issue:**
The hook runs automatically on every session start with no user confirmation.

**Risks:**
- User unaware of what's executing
- No opportunity to review changes
- Silent failures or malicious actions
- 120-second timeout could be abused

**Recommendation:**
- Add confirmation prompt (if not in CI)
- Log what's being executed
- Provide opt-out mechanism

---

### 5. **LOW: Environment Variable Manipulation**

**Risk Level:** 🟢 **LOW**

**Issue:**
The script relies on environment variables:
- `CLAUDE_CODE_REMOTE` (execution gate)
- `CLAUDE_ENV_FILE` (PATH configuration)
- `GH_SETUP_VERSION` (version control)

**Risks:**
- Could be manipulated in compromised environments
- Unexpected behavior if variables are incorrect

**Impact:**
- Limited (mostly causes script to skip or fail)
- Could be used to bypass checks

---

### 6. **LOW: World-Accessible Temporary Directory**

**Risk Level:** 🟢 **LOW**

**Issue:**
From source analysis: "Creates world-accessible temporary directory"

**Risks:**
- Other processes could read downloaded files
- Race condition potential (unlikely in sandboxed environment)

**Recommendation:**
- Use `mktemp -d` with restricted permissions
- Set umask before creating temp directory

---

### 7. **MEDIUM: Unconstrained Network Access**

**Risk Level:** 🟡 **MEDIUM**

**Issue:**
The script requires network access to:
- `github.com`
- `release-assets.githubusercontent.com`

**Current State:**
Network access set to "Full" or must explicitly allow the above domains.

**Risks:**
- Full network access allows other malicious scripts to phone home
- No guarantee the script only accesses GitHub

**Recommendation:**
- Use "Custom" network mode
- Whitelist only required domains:
  - `github.com`
  - `api.github.com`
  - `release-assets.githubusercontent.com`

---

## Package Trust Analysis

### Author Information
- **Username:** oikon48 / oikon
- **Package Age:** Recently created (2026)
- **Community Trust:** Low (23 stars, small user base)
- **Maintenance:** Active (recent updates)

### Red Flags
1. ❌ Not published to npm (GitHub package only)
2. ❌ Small user base (limited peer review)
3. ❌ Single maintainer (bus factor = 1)
4. ⚠️ No verified author identity
5. ⚠️ No official Anthropic endorsement

### Green Flags
1. ✅ Open source (MIT license)
2. ✅ Code is reviewable
3. ✅ Simple, focused functionality
4. ✅ Uses official GitHub sources
5. ✅ Active maintenance

---

## Improvement Recommendations

### Immediate Actions (High Priority)

#### 1. Pin Package Version
```json
{
  "hooks": {
    "SessionStart": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "bun x gh-setup-hooks@2.0.0",
            "timeout": 120
          }
        ]
      }
    ]
  }
}
```

#### 2. Restrict Network Access
In Claude Code settings:
- Change network from "Full" to "Custom"
- Whitelist only:
  - `github.com`
  - `api.github.com`
  - `release-assets.githubusercontent.com`

#### 3. Review Before Updates
- Don't auto-update to new versions
- Review source code changes before upgrading
- Check GitHub for security advisories

---

### Medium-Term Improvements

#### 1. Fork and Self-Host
Create your own fork:
```bash
# Fork the repository
# Review and audit the code
# Publish to your own npm account or GitHub packages
# Update settings.json to use your fork
"command": "bun x your-org/gh-setup-hooks@2.0.0"
```

Benefits:
- Full control over updates
- Can add security improvements
- No dependency on third-party maintainer

#### 2. Alternative: Manual Installation
Replace the hook with a verified binary:
```json
{
  "hooks": {
    "SessionStart": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "curl -fsSL https://github.com/cli/cli/releases/download/v2.83.2/gh_2.83.2_linux_amd64.tar.gz | tar -xz -C ~/.local --strip-components=2 gh_2.83.2_linux_amd64/bin/gh",
            "timeout": 60
          }
        ]
      }
    ]
  }
}
```

Pros:
- No third-party dependency
- Direct from official source
- Faster (no npm package overhead)

Cons:
- No checksum verification in this example
- More complex command
- Harder to maintain

---

### Long-Term Solutions

#### 1. Contribute Security Improvements Upstream
Submit PRs to gh-setup-hooks:
- Make checksum verification blocking
- Add GPG signature verification
- Improve error handling
- Add logging options

#### 2. Request Official Anthropic Package
Ask Anthropic to:
- Create official gh installation package
- Include in default Claude Code environment
- Maintain and security-audit

#### 3. Use Built-in Package Manager
If Claude Code adds package management:
- Use official package registry
- Benefit from security scanning
- Get automatic updates with review

---

## Risk Mitigation Checklist

### For Current Setup

- [ ] **Pin package version** to `gh-setup-hooks@2.0.0`
- [ ] **Review source code** at https://github.com/oikon48/gh-setup-hooks
- [ ] **Restrict network** to Custom mode with whitelisted domains
- [ ] **Monitor package updates** for security changes
- [ ] **Verify gh installation** after each session start
- [ ] **Limit token permissions** (already done - see previous reports)
- [ ] **Document this dependency** in repository README
- [ ] **Set up alerts** for package repository changes

### Best Practices

- [ ] Regular security audits of hooks
- [ ] Keep gh-setup-hooks version documented
- [ ] Test in isolated environment first
- [ ] Have rollback plan if package is compromised
- [ ] Consider alternative installation methods
- [ ] Keep this research document updated

---

## Alternative Solutions

### Option 1: Pre-installed Environment
Request that gh CLI be pre-installed in Claude Code environments (unlikely to be accepted).

### Option 2: Manual Installation Script
Create your own audited installation script in the repository:

```bash
#!/bin/bash
# .claude/install-gh.sh
set -e

VERSION="2.83.2"
ARCH="amd64"
URL="https://github.com/cli/cli/releases/download/v${VERSION}/gh_${VERSION}_linux_${ARCH}.tar.gz"
CHECKSUM_URL="https://github.com/cli/cli/releases/download/v${VERSION}/gh_${VERSION}_checksums.txt"

# Download with verification
curl -fsSL "$URL" -o /tmp/gh.tar.gz
curl -fsSL "$CHECKSUM_URL" -o /tmp/checksums.txt

# BLOCKING verification
cd /tmp && sha256sum -c --ignore-missing checksums.txt || exit 1

# Install
tar -xzf /tmp/gh.tar.gz
mv gh_${VERSION}_linux_${ARCH}/bin/gh ~/.local/bin/
chmod +x ~/.local/bin/gh

# Cleanup
rm -rf /tmp/gh.tar.gz /tmp/checksums.txt /tmp/gh_${VERSION}_linux_${ARCH}
```

Then update settings.json:
```json
{
  "hooks": {
    "SessionStart": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "bash .claude/install-gh.sh",
            "timeout": 60
          }
        ]
      }
    ]
  }
}
```

### Option 3: Container/Image Approach
Use a custom container image with gh pre-installed (if Claude Code supports this).

---

## Conclusion

The `gh-setup-hooks` package serves a legitimate purpose and uses several security best practices. However, there are **significant security risks** that should be addressed:

### Critical Issues
1. ⚠️ Non-blocking checksum verification
2. ⚠️ No code signature verification
3. ⚠️ No version pinning

### Recommended Actions
1. **Immediately:** Pin to version 2.0.0
2. **Soon:** Restrict network access
3. **Consider:** Fork and self-host or create own script

### Overall Assessment
**Current Risk:** 🟡 MEDIUM

With improvements: 🟢 LOW

The package is **usable but requires hardening** for production use.

---

## Sources

- [Run gh Command in Claude Code on the Web - DEV Community](https://dev.to/oikon/run-gh-command-in-claude-code-on-the-web-2kp3)
- [GitHub - oikon48/gh-setup-hooks](https://github.com/oikon48/gh-setup-hooks)
- [GitHub CLI Manual](https://cli.github.com/manual/)
- Package source code analysis from repository

---

**Report Date:** 2026-01-31
**Session:** claude/update-claude-md-JN1pa (main)
**Analyst:** Claude (Sonnet 4.5)
