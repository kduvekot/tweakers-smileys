# SVG Animation Patterns Comparison

## Overview

Tweakers smileys use **CSS-based animations** (not SMIL) for their animated SVGs. This document analyzes the animation patterns used in existing SVGs and how they were applied to create `yes.svg`.

## Existing Animated SVGs

### 1. worshippy.svg - Worship Gesture Animation

**Purpose:** Animated smiley with raised hands in worship gesture, bouncing up and down

**Animation Technique:**
- **4 @keyframes**: `a1`, `a2`, `a2l`, `a2r`
- **Duration:** 2s linear infinite
- **Transforms:** translate, scale, skewX

**Keyframe Breakdown:**

```css
/* Face bounce animation */
@keyframes a1{
  0%,65%,to{transform:translate(0,0) scale(1)}
  15%,50%{transform:translate(0,8px) scale(1,.5)}
}

/* Hands raise and squash */
@keyframes a2{
  0%{transform:translate(0)}
  15%,50%{transform:translate(0,11px) scale(1,.4)}
  65%,to{transform:translate(0) scale(1)}
}

/* Left hand skew for perspective */
@keyframes a2l{
  0%,65%,to{transform:skewX(0)}
  15%,50%{transform:skewX(10deg)}
}

/* Right hand skew for perspective */
@keyframes a2r{
  0%,65%,to{transform:skewX(0)}
  15%,50%{transform:skewX(-10deg)}
}
```

**Key Features:**
- Multiple animations on nested groups
- Squash & stretch effect (scale vertically)
- Skew for 3D-like perspective
- Accessibility: `@media(prefers-reduced-motion){.ani{animation:none}}`

---

### 2. shiny.svg - Sparkle Animation

**Purpose:** Smiley with a twinkling star sparkle effect

**Animation Technique:**
- **1 @keyframe**: `a1`
- **Duration:** 2.6s linear infinite
- **Transform:** scale

**Keyframe Breakdown:**

```css
@keyframes a1{
  69%{transform:scale(0)}        /* Hidden most of the time */
  77%,92%{transform:scale(2)}    /* Pop to 2x size */
  85%{transform:scale(.75)}      /* Bounce back to 0.75x */
}
```

**Key Features:**
- Star hidden 69% of time (creates "twinkle" effect)
- Bounce effect: scale(0) → 2 → 0.75 → 2 (elastic feel)
- Applied to single element (white star path)
- Uses `transform-origin` for anchor point
- Accessibility: `@media(prefers-reduced-motion){*{animation:none!important}}`

---

### 3. yes.svg - Nodding Animation (NEW!)

**Purpose:** Smiley nodding "yes" (vertical head movement)

**Animation Technique:**
- **1 @keyframe**: `nod`
- **Duration:** 0.7s linear infinite
- **Transform:** translateY

**Keyframe Breakdown:**

```css
@keyframes nod{
  0%,57%,to{transform:translateY(0)}      /* At rest */
  14%{transform:translateY(1px)}          /* Down 1px */
  29%{transform:translateY(2px)}          /* Down 2px (peak) */
  43%{transform:translateY(1px)}          /* Up to 1px */
  71%{transform:translateY(-1px)}         /* Slight up movement */
}
```

**Implementation Process:**

1. **Analyzed yes.gif:**
   - 15×15 pixels, 7 frames
   - Vertical nodding motion
   - ~100ms frame delay

2. **Chose CSS over SMIL:**
   - Matches existing pattern (worshippy.svg, shiny.svg)
   - Better browser support
   - Accessibility built-in

3. **Translation values:**
   - Mapped 7 GIF frames to 7 CSS keyframe percentages
   - Small movements (±2px max) for subtle effect at 16×16 size

4. **Timing:**
   - 0.7s duration (faster than worship/shiny for quicker nodding)
   - Keyframe percentages: 0%, 14%, 29%, 43%, 57%, 71%, 100%

---

## Animation Pattern Standards

### Common Structure

All animated Tweakers SVGs follow this pattern:

```svg
<svg xmlns="http://www.w3.org/2000/svg" width="..." height="...">
  <style>
    @keyframes animationName{...}
    @media(prefers-reduced-motion){*{animation:none!important}}
  </style>
  <defs>
    <!-- Gradients, filters, etc -->
  </defs>

  <g style="animation:animationName duration timing iteration">
    <!-- Animated elements -->
  </g>
</svg>
```

### Best Practices Observed

1. **CSS in `<style>` tags** - Not external stylesheets
2. **Inline animation on elements** - `style="animation:..."`
3. **Accessibility first** - Always include `prefers-reduced-motion`
4. **Transform-based** - Use transforms (not position changes) for performance
5. **Percentage keyframes** - More precise timing control than named times
6. **Linear timing** - All use `linear` for consistent frame-by-frame feel
7. **Infinite loops** - Continuous animations

### Transform Types Used

| Transform | Used In | Purpose |
|-----------|---------|---------|
| `translate(x,y)` / `translateY()` | worshippy, yes | Position movement |
| `scale(x,y)` | worshippy, shiny | Size changes, squash/stretch |
| `skewX(deg)` | worshippy | Perspective effect |

---

## GIF → SVG Animation Conversion Guide

### Step-by-Step Process

1. **Analyze GIF frames**
   ```bash
   # Count frames in GIF
   python3 -c "content = open('file.gif', 'rb').read(); print(f'Frames: {content.count(b\"\x2C\")}')"
   ```

2. **Identify motion type**
   - Vertical movement → `translateY()`
   - Horizontal movement → `translateX()`
   - Rotation → `rotate()`
   - Size change → `scale()`
   - Squash/stretch → `scale(x, y)` with different values

3. **Map frames to keyframes**
   - Frame count = keyframe count
   - Distribute percentages evenly (or based on frame delays)

4. **Choose duration**
   - Fast actions: 0.5-1s (nodding, winking)
   - Medium actions: 1-2s (bouncing, waving)
   - Slow actions: 2-3s+ (sparkling, floating)

5. **Add accessibility**
   ```css
   @media(prefers-reduced-motion){*{animation:none!important}}
   ```

6. **Apply to group**
   ```svg
   <g style="animation:name duration linear infinite">
   ```

### Example: yes.gif Conversion

```
yes.gif Analysis:
├─ Dimensions: 15×15 pixels
├─ Frames: 7
├─ Motion: Vertical (nodding down and up)
└─ Frame delays: ~100ms first frame

Conversion Decisions:
├─ Use: translateY() for vertical movement
├─ Duration: 0.7s (7 frames × 100ms)
├─ Keyframes: 7 (matching frame count)
├─ Values: 0 → 1px → 2px → 1px → 0 → -1px → 0
└─ Pattern: CSS animation (matching existing SVGs)

Result:
<g style="animation:nod .7s linear infinite">
  @keyframes nod{
    0%,57%,to{transform:translateY(0)}
    14%{transform:translateY(1px)}
    29%{transform:translateY(2px)}
    43%{transform:translateY(1px)}
    71%{transform:translateY(-1px)}
  }
```

---

## Comparison: SMIL vs CSS

| Aspect | SMIL Animation | CSS Animation |
|--------|----------------|---------------|
| **Syntax** | `<animateTransform>` elements | `@keyframes` + `animation` property |
| **Browser Support** | Deprecated in Chrome (restored), not in IE | Universal modern browser support |
| **Performance** | Good | Better (GPU accelerated) |
| **Accessibility** | Manual pause required | Native `prefers-reduced-motion` |
| **Tweakers Pattern** | ❌ Not used | ✅ Standard pattern |
| **Control** | XML attributes | CSS properties |
| **Complexity** | Verbose XML | Concise CSS |

**Decision:** Use CSS animations to match existing Tweakers pattern.

---

## Animation Candidates from GIF Collection

Unconverted GIFs that could use similar animation patterns:

| GIF | Animation Type | Suggested Transform | Complexity |
|-----|----------------|---------------------|------------|
| **no.gif** | Horizontal shake | `translateX()` | Easy |
| **bye.gif** | Hand waving | `rotate()` or `translateX()` | Medium |
| **lol.gif** | Mouth opening | `scale()` or path morph | Medium |
| **yawnee.gif** | Mouth opening | `scale()` or path morph | Medium |
| **sleepey.gif** | Zzz's floating | `translateY() + opacity` | Easy |
| **shadey.gif** | Static (sunglasses) | None needed | N/A |
| **nosmile.gif** | Static (neutral face) | None needed | N/A |

---

## Learnings from smile.svg → yes.svg

### What Transferred Well

1. **Base template structure** - Yellow gradient, circle, eyes, smile from smile.svg
2. **Same dimensions** - 16×16 viewBox maintains consistency
3. **Modular design** - Easy to swap expressions while keeping animation
4. **Opacity values** - `.9` opacity for soft, consistent appearance

### New Techniques Added

1. **CSS @keyframes** - First time using CSS animation in this conversion
2. **Accessibility support** - `prefers-reduced-motion` media query
3. **Percentage-based timing** - More precise than SMIL's keyTimes
4. **Transform-origin awareness** - Default center works for nodding

### Challenges Solved

1. **Small movements at small size** - Just ±2px is enough for 16×16 canvas
2. **Smooth motion** - 7 keyframes creates natural nodding rhythm
3. **Duration tuning** - 0.7s feels right (not too fast, not too slow)
4. **Keyframe distribution** - Non-linear percentage distribution creates realistic motion

---

## Next Steps

1. Convert `no.gif` using horizontal `translateX()` shake pattern
2. Create animation pattern library for common motions
3. Consider adding subtle animations to static SVGs (eye blinks, etc.)
4. Build automated GIF → SVG animation converter tool

---

## File Locations

- **Animated SVGs:** `tweakers-smileys/svg/worshippy.svg`, `shiny.svg`, `yes.svg`
- **Test page:** `test-yes-animation.html`
- **Original GIFs:** `tweakers-smileys/gif/yes.gif` (current), `tweakers-smileys/old-gif/smile.gif` (legacy)
