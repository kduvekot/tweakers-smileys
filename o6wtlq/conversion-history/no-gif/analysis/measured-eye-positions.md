# Measured Eye Positions from Coalesced Frames

## Left Eye Center Position (measured from black pixels)

```
Frame  | Left Eye X | Right Eye X | Δ from Frame 0 | Direction
-------|------------|-------------|----------------|----------
   0   |    5.5     |     9.5     |      0         | CENTER
   1   |    5.5     |     9.5     |      0         | CENTER (dropped down Y:4→5)
   7   |    7.5     |    11.5     |     +2         | RIGHT
   8   |    6.5     |    10.5     |     +1         | Right
  10   |    4.5     |     8.5     |     -1         | Left
  11   |    3.5     |     7.5     |     -2         | LEFT (maximum!)
  12   |    4.5     |     8.5     |     -1         | Left
  15   |    7.5     |    11.5     |     +2         | RIGHT
  17   |    5.5     |     9.5     |      0         | CENTER
```

## Movement Range

**Horizontal Range:** -2px (left) to +2px (right) = **4px total range**

**Pattern:**
- **Leftmost:** Frame 11 (X = 3.5 and 7.5) = -2px from center
- **Center:** Frames 0, 1, 17 (X = 5.5 and 9.5)
- **Rightmost:** Frames 7, 15 (X = 7.5 and 11.5) = +2px from center

## Vertical Movement

**All shake frames:** Y = 5 (except frame 0 which is Y = 4)

Frame 0 → Frame 1: **Drops down 1 pixel vertically** (Y: 4 → 5)
Frames 1-21: Stay at Y = 5
Loop back to Frame 0: **Jumps up 1 pixel** (Y: 5 → 4)

## Corrected Understanding

The animation is:
1. **Start:** Center position at higher Y (Y=4)
2. **Drop:** Move down 1px (Y=5)
3. **Shake:** Oscillate ±2px horizontally while staying at Y=5
4. **Loop:** Jump back up to starting position

Movement is **±2px horizontally**, not ±4px as I previously thought!

## For SVG Implementation

```
translate(-2px, 1px)  // Leftmost (frame 11)
translate(-1px, 1px)  // Left (frames 10, 12)
translate(0, 0)       // Center high (frame 0)
translate(0, 1px)     // Center low (frames 1, 17)
translate(+1px, 1px)  // Right (frame 8)
translate(+2px, 1px)  // Rightmost (frames 7, 15)
```

The mouth needs to fit within:
- At X=-2: Leftmost position
- At X=+2: Rightmost position

Total movement range: 4px (from -2 to +2)
