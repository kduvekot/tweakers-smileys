# Browser Console Download Instructions

Download all Tweakers smileys using your browser while logged in.

## Method 1: Individual Downloads (RECOMMENDED - No CORS issues!)

This method downloads each smiley as a separate file. Works from any Tweakers page!

1. **Go to any Tweakers.net page** (like gathering.tweakers.net)
2. **Open Chrome DevTools Console**:
   - Press `F12` or `Ctrl+Shift+J` (Windows/Linux)
   - Press `Cmd+Option+J` (Mac)
   - Or right-click anywhere and select "Inspect" → "Console" tab

3. **Copy the entire script** from `download-smileys-bookmarklet.js`

4. **Paste into the console** and press Enter

5. **Allow multiple downloads** - Your browser will ask permission to download multiple files. Click "Allow"

6. **Wait for completion** - The script will:
   - Trigger 64 individual downloads (one per smiley)
   - Each file downloads with its correct name (smile.svg, bonk.gif, etc.)
   - All files go to your Downloads folder

**Tip:** After downloading, create a folder called "tweakers-smileys" and move all the files there.

---

## Method 2: Zip File Download (May have CORS issues)

This method tries to create a single zip file, but may fail due to browser security restrictions.

1. **Log into Tweakers.net** in Google Chrome
2. **Open Chrome DevTools Console**:
   - Press `F12` or `Ctrl+Shift+J` (Windows/Linux)
   - Press `Cmd+Option+J` (Mac)
   - Or right-click anywhere and select "Inspect" → "Console" tab

3. **Copy the entire script** from `download-smileys-console.js`

4. **Paste into the console** and press Enter

5. **Wait for the download** - The script will:
   - Load the JSZip library
   - Try to download all 64 smileys
   - Create a zip file
   - Automatically download `tweakers-smileys.zip` to your Downloads folder

**Note:** If this fails with CORS errors, use Method 1 instead.

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
