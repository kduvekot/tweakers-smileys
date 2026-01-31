#!/usr/bin/env python3
"""
Add cache-busting query parameters to resource URLs in HTML files.
This script injects a version identifier (git commit hash) into all resource
references during the GitHub Actions build process.

Usage:
    python3 add-cache-busting.py --source-dir <dir> --version <version>
"""

import os
import re
import sys
import argparse
from pathlib import Path
from typing import Optional


def add_cache_busting_to_html(content: str, version: str) -> str:
    """
    Add cache-busting query parameters to resource references in HTML.

    This handles ANY file type with an extension:
    - Static resources: <link href="style.css"> -> <link href="style.css?v=VERSION">
    - JavaScript: <script src="app.js"> -> <script src="app.js?v=VERSION">
    - Images: <img src="image.png"> -> <img src="image.png?v=VERSION">
    - Media: <video src="video.mp4"> -> <video src="video.mp4?v=VERSION">
    - Any extension: .css, .js, .png, .mp3, .wav, .mp4, .pdf, .zip, etc.
    - Inline JS: Inject version constant for dynamic URL construction
    """

    # Resource extensions that should get cache-busting
    # Match ANY file with an extension (generic pattern)
    resource_extensions = r'\.[a-zA-Z0-9_-]+'

    # Pattern 1: href and src attributes (static resources)
    # <link href="file.css"> or <img src="image.png">
    # Skip URLs that already have ?v= in them
    content = re.sub(
        r'((?:href|src)=["\'])([^"\']*?' + resource_extensions + r')(?!\?v=)(["\'])',
        lambda m: m.group(1) + m.group(2) + f'?v={version}' + m.group(3),
        content,
        flags=re.IGNORECASE
    )

    # Pattern 2: Inject cache-busting version into inline JavaScript
    # Look for the script tag that contains loadSmileys function and inject a version constant
    if 'loadSmileys' in content:
        # Find the opening of the script tag and inject a version constant right after it
        script_pattern = r'(<script[^>]*>)'
        if re.search(script_pattern, content):
            # Inject version constant at the start of the script
            version_declaration = f'\n        const CACHE_BUST_VERSION = "{version}";\n'
            content = re.sub(
                script_pattern,
                r'\1' + version_declaration,
                content,
                count=1,
                flags=re.IGNORECASE
            )

            # Now update the dynamic image loading to use the version
            # Pattern: img.src = `...` to img.src = `...?v=VERSION`
            # But only add if not already present
            content = re.sub(
                r'(img\.src = `([^`]*' + resource_extensions + r')`)(?!.*\?v=)',
                r'\1 + "?v=" + CACHE_BUST_VERSION + "`',
                content,
                flags=re.IGNORECASE
            )

            # Also handle format: img.src = `${type.dir}/${filename}`
            # We need to add the version to the fetch calls or image URLs
            # Better approach: modify the image src assignment
            content = re.sub(
                r'(\s+img\.src\s*=\s*)`([^`]+)`',
                lambda m: m.group(1) + '`' + m.group(2) + '?v=${CACHE_BUST_VERSION}' + '`',
                content
            )

    return content


def process_html_files(source_dir: str, version: str) -> tuple[int, int]:
    """
    Process all HTML files in the source directory.

    Args:
        source_dir: Root directory containing HTML files
        version: Version identifier (e.g., commit hash)

    Returns:
        Tuple of (files_processed, files_modified)
    """
    files_processed = 0
    files_modified = 0

    html_files = Path(source_dir).rglob('*.html')

    for html_file in html_files:
        files_processed += 1

        try:
            # Read the file
            with open(html_file, 'r', encoding='utf-8') as f:
                original_content = f.read()

            # Add cache-busting
            modified_content = add_cache_busting_to_html(original_content, version)

            # Only write if changed
            if modified_content != original_content:
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(modified_content)
                files_modified += 1
                print(f"✓ Modified: {html_file}")
            else:
                print(f"  No changes: {html_file}")

        except Exception as e:
            print(f"✗ Error processing {html_file}: {e}", file=sys.stderr)
            return files_processed, files_modified

    return files_processed, files_modified


def main():
    parser = argparse.ArgumentParser(
        description='Add cache-busting query parameters to HTML resource URLs'
    )
    parser.add_argument(
        '--source-dir',
        required=True,
        help='Directory containing HTML files to process'
    )
    parser.add_argument(
        '--version',
        required=True,
        help='Version identifier (e.g., git commit hash or timestamp)'
    )

    args = parser.parse_args()

    # Verify source directory exists
    if not Path(args.source_dir).exists():
        print(f"Error: Source directory not found: {args.source_dir}", file=sys.stderr)
        sys.exit(1)

    # Process files
    print(f"Adding cache-busting with version: {args.version}")
    print(f"Processing directory: {args.source_dir}")
    print()

    processed, modified = process_html_files(args.source_dir, args.version)

    print()
    print(f"Summary: {processed} file(s) processed, {modified} file(s) modified")

    if modified == 0:
        print("No HTML files with resources were found or modified.")

    sys.exit(0)


if __name__ == '__main__':
    main()
