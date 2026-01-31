# Re-interpretation of GIF Geometry Data

## The Confusion

I misinterpreted what the X-offset means in GIF frame geometry.

## GIF Frame Encoding

```
Frame 0: 15x15 at +0+0   (full image)
Frame 1: 11x8 at +3+4    
Frame 7: 10x7 at +4+5    
```

## What I Thought It Meant

"The face moves +4 pixels to the RIGHT"

## What It Actually Means

The +X offset is where the CANVAS BOUNDING BOX is placed, but the face INSIDE that box can be positioned anywhere!

When extracting with `-coalesce`, ImageMagick reconstructs the full frames by:
1. Taking the previous frame as base
2. Overlaying the new content block at the specified offset
3. Creating a complete 15x15 image

## The Real Movement Pattern

Looking at the actual extracted frames visually:
- **Frame 0:** Face CENTERED
- **Frame 1:** Face moved RIGHT
- **Frame 2:** Face moved RIGHT (less)
- **Frame 7:** Face moved LEFT (maximum!)
- **Frame 15:** Face moved LEFT (maximum!)

The face DOES move both left and right!

## Why The Canvas Offsets Are All Positive

The GIF encoder is optimizing by only storing changed regions. The bounding box offset doesn't directly correspond to feature movement direction - it's just telling where to paste the content block on the canvas.

The actual FACE movement inside those blocks goes BOTH directions.

## Correct Movement Analysis Required

Need to measure actual eye/mouth positions in the coalesced frames, not rely on the GIF's internal encoding metadata!
