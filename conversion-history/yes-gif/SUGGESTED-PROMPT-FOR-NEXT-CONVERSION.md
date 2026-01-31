# Prompt: Converting Animated GIF Smiley to SVG

## Context

You're converting an animated GIF smiley from the Tweakers forum collection to an animated SVG format. The Tweakers collection has established standards and patterns you must follow for consistency.

## Critical Standards (MUST FOLLOW)

### Canvas Size
- **Always use 16×16** for the SVG canvas
- Even if the original GIF is 15×15 (legacy format), upscale to 16×16
- This is the standard across the entire SVG collection

### Standard Components

**Eyes (for regular round eyes):**
```svg
<rect width="2" height="2" rx=".5" fill="#000" fill-opacity=".9"/>
```
- Position varies by smiley, but dimensions are always 2×2 with rx=.5
- Used by: smile.svg, biggrin.svg, wink.svg, confused.svg, unhappy.svg

**Smile Mouth (for happy smileys):**
```svg
<path d="M12.75 7.75c-.1.75-.8 2.04-2.17 2.5-.75.25-1.33.25-2.33.25m-4.5-2.75c.1.75.8 2.04 2.17 2.5.75.25 1.33.25 2.33.25"
      stroke="#000" stroke-opacity=".9" stroke-width="1.1"/>
```
- This is the standard smile path used across multiple smileys

**Yellow Face (16×16 standard):**
```svg
<radialGradient id="a" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse"
                gradientTransform="rotate(59.99 .72 5.4) scale(12.7918)">
  <stop stop-color="#FAFAE3"/>
  <stop offset=".23" stop-color="#FFFFA2"/>
  <stop offset=".66" stop-color="#FFEF06"/>
  <stop offset="1" stop-color="#C7B300"/>
</radialGradient>

<circle cx="8" cy="8" r="7.9" fill="url(#a)"/>
<circle cx="8" cy="8" r="7.63" stroke="#000" stroke-opacity=".9" stroke-width=".75"/>
```

## Methodology

### Step 1: Frame Extraction
```bash
# Extract all frames from animated GIF
convert input.gif -coalesce frames/frame-%d.png

# Analyze frame count
identify input.gif | wc -l
```

### Step 2: Frame Analysis
- Examine each frame at high magnification (10x or more)
- Identify what elements move vs stay static
- Measure pixel-level changes between frames
- Look for:
  - **Vertical/horizontal translation** (elements moving position)
  - **Scaling effects** (elements changing size, especially height)
  - **Shape changes** (eyes squinting, mouth shape changes)

### Step 3: Check Existing Collection
**IMPORTANT:** Before creating custom components, check if similar elements exist:
```bash
# Find similar smileys
ls /path/to/tweakers-smileys/svg/

# Examine their structure
cat smile.svg wink.svg biggrin.svg
```

Look for reusable patterns - don't reinvent the wheel!

### Step 4: Animation Pattern (Validated Approach)

The `worshippy.svg` file validates the best animation approach:

**Unified Group Animation (PREFERRED):**
```svg
<g class="face-features">
    <rect x="5.5" y="4" width="2" height="2" rx=".5" fill="#000" fill-opacity=".9"/>
    <rect x="9.5" y="4" width="2" height="2" rx=".5" fill="#000" fill-opacity=".9"/>
    <path d="[mouth path]" stroke="#000" stroke-opacity=".9" stroke-width="1.1"/>
</g>

<style>
@keyframes animate-face {
    0%, 100% { transform: translate(0, 0) scale(1, 1); }
    50% { transform: translate(0, Ypx) scale(1, 0.5); }
}
.face-features {
    animation: animate-face 0.7s infinite;
    transform-origin: center;
}
</style>
```

**Why unified?**
- More natural motion (all features compress together)
- Matches worshippy.svg pattern (already in production)
- Simpler code
- More expressive

**When to use separate animations:**
- If mouth and eyes move at different rates
- If mouth doesn't change shape during animation
- If you need independent control

### Step 5: Key Animation Parameters

**Translation distance** depends on semantic meaning:
- **Gentle nod (yes):** ~4-5px vertical movement
- **Deep bow (worshippy):** ~8px vertical movement
- **Shake (no):** Horizontal movement instead

**Scale effects:**
- `scale(1, 0.5)` = 50% vertical compression (squinting/flattening)
- Applied at the peak/trough of the motion
- Affects ALL elements in the group

**Timing:**
- Standard duration: **0.7s** seems to work well
- Use `infinite` for continuous loop
- Include `@media (prefers-reduced-motion: reduce)` for accessibility

## Validation Approach

### Visual Comparison
```bash
# Render SVG to same size as GIF for comparison
convert your-animated.svg -resize WxH\! test.png

# Side-by-side comparison
convert original.gif test.png +append comparison.png
```

### RMSE Validation (Optional)
```bash
# Compare individual frames
convert frame-0-final.svg -resize 15x15\! frame-0-test.png
compare -metric RMSE frames/frame-0.png frame-0-test.png diff.png
```
- RMSE < 0.5 is excellent
- RMSE < 0.6 is acceptable for pixel art at this scale

## Common Pitfalls to Avoid

1. **DON'T assume 15×15** - Always check standards first (it's 16×16)
2. **DON'T create custom eyes** - Use standard 2×2 rx=.5 unless special case
3. **DON'T ignore existing smileys** - They contain reusable patterns
4. **DON'T just translate** - Look for scaling/squishing effects too
5. **DON'T forget stable outline** - Face circle should NOT animate (use static elements)
6. **DON'T skip accessibility** - Include prefers-reduced-motion media query

## File Organization

```
[smiley-name]-conversion/
├── frames/
│   └── frame-*.png (extracted GIF frames)
├── svg-frames/
│   └── frame-*-final.svg (individual SVG frames for reference)
├── [smiley-name]-animated.svg (final animated version)
├── [smiley-name]-animation-demo.html (comparison demo)
└── logs/
    └── *.md (documentation of process and learnings)
```

## Expected Output

Deliver:
1. **Animated SVG file** using standard components and unified animation
2. **Demo HTML page** showing GIF vs SVG comparison
3. **Documentation** in logs/ explaining approach and findings
4. **Frame SVGs** (optional, for reference/debugging)

## Quick Checklist

- [ ] Canvas is 16×16
- [ ] Eyes use standard 2×2 rx=.5 (if applicable)
- [ ] Gradient uses standard scale(12.7918) (if yellow face)
- [ ] Face circles are r=7.9 and r=7.63 (if applicable)
- [ ] Animation uses unified group approach (unless good reason)
- [ ] Includes `@media (prefers-reduced-motion: reduce)`
- [ ] Face outline is static (doesn't animate)
- [ ] Created demo page showing comparison
- [ ] Documented process in logs/

## Example Command Flow

```bash
# 1. Extract frames
convert input.gif -coalesce frames/frame-%d.png

# 2. Analyze at high magnification
convert frames/frame-0.png -scale 1000% frames/frame-0-mega.png

# 3. Check existing standards
grep -r "width=\"2\" height=\"2\"" ../tweakers-smileys/svg/

# 4. Create animated SVG (use unified group approach)
# [manual creation based on analysis]

# 5. Create demo page
# [create HTML with side-by-side comparison]

# 6. Document findings
# [create log entry in logs/ directory]
```

## Success Criteria

✅ Visual match: Looks like the original GIF in motion
✅ Standard compliance: Uses 16×16 and standard components where applicable
✅ Pattern validation: Animation approach matches worshippy.svg style
✅ Scalability: Looks good at 16×16, 32×32, 64×64, etc.
✅ Documentation: Process and learnings captured in logs/

Good luck! Remember: **Check standards first, analyze carefully, use unified animation, document everything.**
