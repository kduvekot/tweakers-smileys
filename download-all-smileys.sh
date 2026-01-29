#!/bin/bash
# Tweakers Smiley Downloader - Shell Script
# This script downloads all 64 Tweakers smileys to the current directory
# Usage: bash download-all-smileys.sh

echo "🎨 Tweakers Smiley Downloader"
echo "================================"
echo ""

# Create output directory
OUTPUT_DIR="tweakers-smileys"
mkdir -p "$OUTPUT_DIR"

echo "📂 Created directory: $OUTPUT_DIR"
echo "📥 Downloading 64 smileys..."
echo ""

# Array of all smiley files
declare -a smileys=(
    "smile.svg" "frown.svg" "unhappy.svg" "wink.svg" "devil.svg" "puh.svg" "puh2.svg"
    "yummie.svg" "redface.svg" "shiny.svg" "cry.svg" "coool.svg" "clown.svg"
    "biggrin.svg" "worshippy.svg" "kwijl.svg" "heart.svg" "yawnee.gif" "rc5.svg"
    "nosmile2.svg" "shutup.gif" "confused.svg" "bonk.gif" "frusty.gif" "hypocrite.gif"
    "sleephappy.gif" "sadley.svg" "facepalm.gif" "tweakers.svg" "henk.svg" "nosmile.gif"
    "farewell.gif" "pukey.gif" "nerd.svg" "vork.svg" "michel.svg" "loveit.svg"
    "sleepey.gif" "devilish.svg" "shadey.gif" "bye.gif" "thumbsup.svg" "ok.svg"
    "bonk3.gif" "loveys.gif" "sintsmiley.gif" "xmas.svg" "marrysmile.svg" "bloos.svg"
    "eerie.svg" "emo.svg" "huh.svg" "yes.gif" "no.gif" "pompom.gif" "nopompom.gif"
    "lol.gif" "hup.gif" "oranje.gif" "belgie.gif" "paard.svg" "rozewolk.gif"
    "knuf.gif" "yummie-beer.svg"
)

BASE_URL="https://tweakers.net/g/s"

# Download counter
count=0
success=0
failed=0

# Download each smiley
for smiley in "${smileys[@]}"; do
    count=$((count + 1))
    printf "[%2d/64] Downloading %s... " "$count" "$smiley"

    if curl -s -f -o "$OUTPUT_DIR/$smiley" "$BASE_URL/$smiley"; then
        echo "✅"
        success=$((success + 1))
    else
        echo "❌"
        failed=$((failed + 1))
    fi
done

echo ""
echo "================================"
echo "📊 Download Summary:"
echo "   ✅ Success: $success"
echo "   ❌ Failed: $failed"
echo ""
echo "📂 Files saved to: $OUTPUT_DIR/"
echo ""

if [ $success -gt 0 ]; then
    echo "✅ Download complete! Check the '$OUTPUT_DIR' folder."
else
    echo "❌ No files were downloaded. Please check your internet connection."
fi
