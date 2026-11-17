# LoL Smiley Timing Analysis

## Frame Timing Data

```
Frame 0: 10ms
Frame 1: 10ms
Frame 2: 10ms
Frame 3: 10ms
Frame 4: 10ms
Frame 5: 10ms
```

## Duration Calculation

- All frames have uniform 10ms delay
- Total frames: 6
- Total duration: 6 × 10ms = 60ms = 0.06s
- This is a very fast animation!

## Frame Duplication Analysis

Total frames: 6
Unique frames: 4

Duplicate patterns:
- Frame 0: unique
- Frame 1: unique (also appears as frame 5)
- Frame 2: unique (also appears as frame 4)
- Frame 3: unique

Sequence: 0, 1, 2, 3, 2, 1 (creates a smooth back-and-forth cycle)

## Keyframe Percentages

For SVG animation with uniform timing:
- Frame 0: 0% (0ms)
- Frame 1: 16.67% (10ms)
- Frame 2: 33.33% (20ms)
- Frame 3: 50% (30ms)
- Frame 4: 66.67% (40ms)
- Frame 5: 83.33% (50ms)
- Loop: 100% (60ms) → back to frame 0

## Animation Pattern

The animation cycles: 0 → 1 → 2 → 3 → 2 → 1 → repeat
This creates a smooth oscillating effect.
