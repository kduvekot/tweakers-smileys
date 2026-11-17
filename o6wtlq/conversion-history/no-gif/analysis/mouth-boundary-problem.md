# Mouth Going Outside Circle - Analysis

## Problem

When the animation translates the features by ±4px horizontally, the mouth corners go outside the face circle.

## Current Mouth Path

```svg
M13.25 11.25C13 9 12 8.4 10.83 8c-.75-.25-1.33-.25-2.33-.25m-4.75 3.5C4 9 5 8.4 6.17 8c.75-.25 1.33-.25 2.33-.25
```

**Key Points:**
- Right corner start: (13.25, 11.25)
- Left corner start: (3.75, 11.25)

## Circle Boundaries

Circle: cx="8" cy="8" r="7.9"

At Y=11.25:
- x = 8 ± sqrt(7.9² - (11.25-8)²)  
- x = 8 ± sqrt(62.41 - 10.5625)
- x = 8 ± 7.2
- **Valid range: X = 0.8 to 15.2**

## Static Position (translate(0, 0))

- Right corner: X=13.25 ✓ INSIDE (< 15.2)
- Left corner: X=3.75 ✓ INSIDE (> 0.8)

## Problem: At Max Right translate(4px, 1px)

After translation:
- Right corner: (13.25 + 4, 11.25 + 1) = **(17.25, 12.25)** ❌

At Y=12.25:
- x = 8 ± sqrt(7.9² - (12.25-8)²)
- x = 8 ± sqrt(44.35)
- x = 8 ± 6.66
- Valid range: X = 1.34 to **14.66**

**Right corner at X=17.25 is 2.59px OUTSIDE the circle!**

## Problem: At Max Left translate(-4px, 1px)

After translation:
- Left corner: (3.75 - 4, 11.25 + 1) = **(-0.25, 12.25)** ❌

At Y=12.25, valid range starts at X=1.34

**Left corner at X=-0.25 is 1.59px OUTSIDE the circle!**

## Solution

The mouth needs to be narrower in the base SVG so that even when translated ±4px, it stays inside the circle.

**Required adjustments:**
- Right corner: Must be at X ≤ 14.66 - 4 = **10.66** (currently 13.25, too far right!)
- Left corner: Must be at X ≥ 1.34 + 4 = **5.34** (currently 3.75, too far left!)

**New mouth width:**
- Should span approximately X = 5.34 to 10.66
- Current span: 3.75 to 13.25 (9.5px wide)
- New span: 5.34 to 10.66 (5.32px wide)
- **Need to make mouth ~44% narrower!**

Or more conservatively, to stay safely inside:
- Right corner: X ≤ 11 (leaves 3.66px margin when at max right)
- Left corner: X ≥ 5 (leaves 1.66px margin when at max left)
- **New mouth width: 6px (from 5 to 11)**

This is a significantly narrower mouth, but necessary to keep it inside the circle during the full range of motion.
