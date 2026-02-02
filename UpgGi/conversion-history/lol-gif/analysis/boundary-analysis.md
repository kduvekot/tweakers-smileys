# LoL Smiley Boundary Analysis

## Canvas Specifications

For a double-width smiley:
- Canvas: 32×16 pixels
- Left face center: (8, 8) with radius ~7.63
- Right face center: (24, 8) with radius ~3.5 to 4 (smaller face)

## Movement Boundaries

Small right face bounces vertically:
- Starting position: Y = 0px offset
- Maximum downward: Y = +6px or +7px offset

Need to verify:
1. Does the small face fit within canvas at lowest position (Y+7)?
2. What is the exact radius of the small face?

## Small Face at Extreme Positions

If small face center is at (24, 8) with radius 3.5:
- Top boundary: Y = 8 - 3.5 = 4.5
- Bottom boundary: Y = 8 + 3.5 = 11.5

At maximum downward movement (+7px):
- New center: (24, 15)
- New bottom boundary: 15 + 3.5 = 18.5

Canvas height is 16, so 18.5 > 16 ❌ 

This suggests either:
1. The small face is smaller than radius 3.5
2. The small face starts higher (center not at Y=8)
3. The movement is less than 7px
4. The small face is allowed to go partially off-canvas

Need to measure the actual face positions and sizes from frame 0.
