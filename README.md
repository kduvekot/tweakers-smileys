# Tweakers Smileys Downloader

Download all 64 Tweakers forum smileys (44 SVG + 20 GIF files) easily.

## Quick Start (EASIEST METHOD) ⭐

### Option 1: Direct Download (Easiest!)

**All smileys are already included in this repository!**

Just download **`tweakers-smileys.zip`** from this repo - it contains all 64 smileys ready to use.

### Option 2: Shell Script

**Works on Linux, Mac, WSL, or Git Bash on Windows**

```bash
bash download-all-smileys.sh
```

That's it! All 64 smileys will be downloaded to a `tweakers-smileys/` folder.

### Option 3: Open HTML Page Locally

1. Open `download-page.html` in your browser (double-click the file)
2. Click "Download All Smileys" button
3. Allow multiple downloads when prompted
4. All files download to your Downloads folder

**Note:** This works best when the HTML file is opened as `file://` from your local computer.

---

## Alternative Methods

### Browser Console Scripts

See [BROWSER_DOWNLOAD_INSTRUCTIONS.md](BROWSER_DOWNLOAD_INSTRUCTIONS.md) for detailed instructions on using JavaScript console scripts.

**Note:** Browser console methods may encounter CORS (Cross-Origin Resource Sharing) issues when running from `gathering.tweakers.net`. The shell script method above is more reliable.

---

## What You Get

All 64 Tweakers smileys **PLUS 35 legacy GIF versions**:
- 38 SVG files (scalable vector graphics) - current versions
- 26 GIF files (animated images) - current versions
- 35 old GIF files (legacy versions of current SVGs)

**Total: 99 smiley files** organized into folders:
- `svg/` - Current SVG versions
- `gif/` - Current animated GIFs
- `old-gif/` - Legacy GIF versions (discovered via testing)

Each file is named according to its original filename:
- Current: `smile.svg`, `frown.svg`, `bonk.gif`, `facepalm.gif`, etc.
- Legacy: `smile.gif`, `frown.gif`, `heart.gif`, etc. (in `old-gif/` folder)

See `old-gif/README.md` in the zip for details about the legacy versions.

---

## Reference

See [SMILEY_REFERENCE.md](SMILEY_REFERENCE.md) for a complete list of all smileys with their codes and direct links.

---

## Requirements

- **Shell script:** `curl` (pre-installed on most systems)
- **HTML page:** Modern web browser (Chrome, Firefox, Edge, Safari)
- **Browser console:** Chrome/Edge browser with DevTools

---

## Troubleshooting

**Shell script shows "command not found":**
- Make sure you have `curl` installed: `which curl`
- Install curl: `sudo apt install curl` (Ubuntu/Debian) or `brew install curl` (Mac)

**HTML page downloads fail:**
- Your browser may block multiple downloads. Check browser settings to allow multiple downloads.
- Some browsers require user interaction for each download when cross-origin.

**Browser console scripts fail with CORS errors:**
- Use the shell script method instead, or
- Open the HTML page locally, or
- Install a CORS-bypass browser extension (not recommended for security reasons)

---

## License

These smileys are property of Tweakers.net. This repository provides tools to download them for personal use.
