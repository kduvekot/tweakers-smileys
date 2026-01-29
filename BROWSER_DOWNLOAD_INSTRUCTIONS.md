# Browser Console Download Instructions

Download all Tweakers smileys using your browser while logged in.

## Quick Start

1. **Log into Tweakers.net** in Google Chrome
2. **Open Chrome DevTools Console**:
   - Press `F12` or `Ctrl+Shift+J` (Windows/Linux)
   - Press `Cmd+Option+J` (Mac)
   - Or right-click anywhere and select "Inspect" → "Console" tab

3. **Copy the entire script** from `download-smileys-console.js`

4. **Paste into the console** and press Enter

5. **Wait for the download** - The script will:
   - Load the JSZip library
   - Download all 64 smileys using your logged-in session
   - Create a zip file
   - Automatically download `tweakers-smileys.zip` to your Downloads folder

## What It Does

- Downloads all 64 Tweakers smileys (44 SVGs + 20 GIFs)
- Uses your existing login session (no authentication needed)
- Shows progress in the console for each smiley
- Creates a single `tweakers-smileys.zip` file with all images
- Each file is named according to its original filename (e.g., `smile.svg`, `bonk.gif`)

## Console Output

You'll see output like this:
```
🎨 Tweakers Smiley Downloader Starting...
📦 Loading JSZip library...
✅ JSZip loaded successfully
📥 Downloading 64 smileys...
[1/64] Fetching smile.svg...
[2/64] Fetching frown.svg...
...
📊 Download Summary:
   ✅ Success: 64
   ❌ Failed: 0

📦 Creating zip file...
✅ Download started! Check your downloads folder for tweakers-smileys.zip
```

## Troubleshooting

- **CORS errors**: Make sure you're running the script while on tweakers.net domain
- **401/403 errors**: Ensure you're logged into your Tweakers account
- **Script blocked**: Some browser extensions may block scripts - try disabling them temporarily
- **Download blocked**: Check your browser's download permissions

## File Contents

After extraction, you'll have all smileys organized as:
- `smile.svg`, `frown.svg`, `wink.svg`, etc.
- `bonk.gif`, `facepalm.gif`, `pompom.gif`, etc.

Total: 64 files (44 SVG + 20 GIF)
