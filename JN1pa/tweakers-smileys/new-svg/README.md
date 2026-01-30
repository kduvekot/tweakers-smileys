# New SVG Conversions

This directory contains **newly converted SVG files** created from the GIF versions in the `gif/` folder.

## Purpose

To separate newly created SVG conversions from the existing SVG files that were already part of the Tweakers smiley collection. This prevents confusion and makes it clear which files are new conversions.

## Files in this folder

- **yes.svg** - Converted from `gif/yes.gif` with nodding animation (CSS @keyframes)

## Conversion Approach

All new SVGs follow the established Tweakers pattern:
- Base template from `smile.svg` (yellow gradient, 16×16, consistent structure)
- CSS animations using `@keyframes` (matching `worshippy.svg`, `shiny.svg`)
- Accessibility support with `prefers-reduced-motion` media queries
- Transform-based animations for performance

## Comparison

| Folder | Files | Description |
|--------|-------|-------------|
| `svg/` | 38 | Original SVG versions from Tweakers |
| `new-svg/` | 1+ | New GIF→SVG conversions |
| `gif/` | 26 | Current GIF versions (not yet converted) |
| `old-gif/` | 35 | Legacy GIF versions of current SVGs |

## See Also

- **ANIMATION_COMPARISON.md** - Detailed analysis of animation patterns
- **test-yes-animation.html** - Test page for comparing GIF vs SVG
