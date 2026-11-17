# New SVG Conversions

This directory contains our own **LLM-made SVG conversions** (January 2026) of three animated GIF smileys, now in `../old-gif/`.

> **Update, 17 November 2026:** Tweakers has since released official SVG versions of all three (and of every other smiley). Those are in `../svg/`. These files are kept for comparison: the archive's [index page](../../index.html) shows the original GIF, our version and the official one side by side.

## Purpose

To separate newly created SVG conversions from the existing SVG files that were already part of the Tweakers smiley collection. This prevents confusion and makes it clear which files are new conversions.

## Files in this folder

- **yes.svg** - Converted from `yes.gif`, nodding animation (CSS @keyframes)
- **no.svg** - Converted from `no.gif`, head-shake animation
- **lol.svg** - Converted from `lol.gif`, double-width laughing animation

## Conversion Approach

All new SVGs follow the established Tweakers pattern:
- Base template from `smile.svg` (yellow gradient, 16×16, consistent structure)
- CSS animations using `@keyframes` (matching `worshippy.svg`, `shiny.svg`)
- Accessibility support with `prefers-reduced-motion` media queries
- Transform-based animations for performance

## Comparison

| Folder | Files | Description |
|--------|-------|-------------|
| `svg/` | 64 | Official Tweakers SVGs (complete set, Nov 2026) |
| `new-svg/` | 3 | Our own GIF → SVG conversions (Jan 2026) |
| `old-gif/` | 61 | Legacy GIF versions |

## See Also

- **../../conversion-history/yes-gif/ANIMATION_COMPARISON.md** - Detailed analysis of animation patterns
- **../../conversion-history/yes-gif/test-yes-animation.html** - Test page for comparing GIF vs SVG
