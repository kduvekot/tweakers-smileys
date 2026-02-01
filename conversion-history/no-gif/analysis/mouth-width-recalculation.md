# Mouth Width Recalculation

## Discovery: Movement is ±2px, not ±4px!

After measuring actual eye positions in coalesced frames:
- **Leftmost:** -2px from center (frame 11)
- **Rightmost:** +2px from center (frames 7, 15)
- **Total range:** 4px (-2 to +2)

## Circle Boundary at Mouth Level

Mouth at approximately Y=10.5-11.25:
- Circle: cx=8, cy=8, r=7.9
- At Y=10.5: x = 8 ± sqrt(7.9² - 2.5²) = 8 ± 7.49
- **Valid X range: 0.51 to 15.49**

## Original Mouth Width Check

Original mouth path:
- Left corner: X ≈ 3.75
- Right corner: X ≈ 13.25

With ±2px movement:
- **Left extreme:** 3.75 - 2 = 1.75 ✓ (INSIDE 0.51 boundary!)
- **Right extreme:** 13.25 + 2 = 15.25 ✓ (INSIDE 15.49 boundary!)

## Conclusion

**The original mouth width was FINE!**

I unnecessarily narrowed it when I thought the movement was ±4px. With the correct ±2px range, the original unhappy.svg mouth path fits perfectly and stays within the circle during the full range of motion.

## Mouth Width Decision

**Restore original width:** X = 3.75 to 13.25 (from unhappy.svg)

No need for the narrowed version!
