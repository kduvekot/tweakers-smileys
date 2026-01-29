#!/usr/bin/env python3
"""Generate a JSON file listing all smileys for the index page."""

import json
import os
from pathlib import Path

def generate_smiley_list():
    """Generate a JSON file with all smiley information."""

    base_dir = Path(__file__).parent.parent / "tweakers-smileys"

    categories = {
        "svg": {
            "label": "SVG Smileys (Current)",
            "files": []
        },
        "gif": {
            "label": "Animated GIF Smileys (Current)",
            "files": []
        },
        "old-gif": {
            "label": "Legacy GIF Smileys",
            "files": [],
            "legacy": True
        }
    }

    # Scan each directory
    for category, info in categories.items():
        dir_path = base_dir / category
        if dir_path.exists():
            # Get all files with the expected extension
            ext = "svg" if category == "svg" else "gif"
            files = sorted([
                f.name for f in dir_path.iterdir()
                if f.is_file() and f.suffix.lower() == f".{ext}"
            ])
            info["files"] = files

    # Output the JSON
    output_path = base_dir.parent / "smileys.json"
    with open(output_path, 'w') as f:
        json.dump(categories, f, indent=2)

    print(f"Generated {output_path}")
    print(f"  SVG: {len(categories['svg']['files'])} files")
    print(f"  GIF: {len(categories['gif']['files'])} files")
    print(f"  Old GIF: {len(categories['old-gif']['files'])} files")

if __name__ == "__main__":
    generate_smiley_list()
