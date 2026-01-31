# Mouth Going Outside Circle on Right Side

## The Problem

At rightmost position (translate(+2px, 1px)), the mouth's right corner goes outside the circle, but the left corner stays inside at leftmost position.

## Circle Boundaries

Circle: cx=8, cy=8, r=7.9

## Mouth Position After Translation

**Right corner:** starts at (13.25, 11.25)
At rightmost: (13.25 + 2, 11.25 + 1) = **(15.25, 12.25)**

**Left corner:** starts at (3.75, 11.25)  
At leftmost: (3.75 - 2, 11.25 + 1) = **(1.75, 12.25)**

## Circle Boundary at Y=12.25

x = 8 ± sqrt(7.9² - (12.25-8)²)
x = 8 ± sqrt(62.41 - 18.06)
x = 8 ± sqrt(44.35)
x = 8 ± 6.66

**Valid X range: 1.34 to 14.66**

## Boundary Check

**Left corner at leftmost:**
- Position: X = 1.75
- Boundary: X ≥ 1.34
- Status: 1.75 > 1.34 ✓ **INSIDE**

**Right corner at rightmost:**
- Position: X = 15.25
- Boundary: X ≤ 14.66
- Status: 15.25 > 14.66 ✗ **OUTSIDE by 0.59px!**

## Why Asymmetric?

The mouth path from unhappy.svg isn't perfectly centered:
- Right corner: 13.25 (5.25px from center at x=8)
- Left corner: 3.75 (4.25px from center at x=8)

The mouth is shifted 0.5px to the right of center!

## Solution

Need to move the mouth slightly left to center it, OR make the right side narrower.

**Option 1:** Shift entire mouth left by 0.3-0.5px
**Option 2:** Make mouth narrower on right side only
**Option 3:** Make mouth symmetrically narrower (both sides)

With ±2px movement, safe mouth corner positions should be:
- Right corner: X ≤ 14.66 - 2 = **12.66** (currently 13.25)
- Left corner: X ≥ 1.34 + 2 = **3.34** (currently 3.75 ✓)

Need to reduce right corner by ~0.6px.
