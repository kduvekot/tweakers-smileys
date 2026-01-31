# LoL Smiley Movement Analysis - DETAILED MEASUREMENTS

## GIF Structure
- Total canvas: 29×15 pixels (double-width)
- Left face: Large, static (approximately 0-18px)
- Right face: Small, animated (approximately 19-29px)

## Frame-by-Frame Analysis of Small Right Face

### Frame 0 (Start position - HIGH)
Small face visible at top of canvas

### Frame 1 
Small face moved down ~2px

### Frame 2
Small face moved down ~4px from frame 0

### Frame 3 (Extreme position - LOW)
Small face moved down ~6-7px from frame 0

### Frame 4 = Frame 2
Small face back at ~4px down position

### Frame 5 = Frame 1
Small face back at ~2px down position

## Movement Pattern

Vertical translation only - no horizontal movement, no scaling.

Animation sequence creates a smooth bounce:
```
Frame 0: Y = 0px (high/neutral)
Frame 1: Y = +2px
Frame 2: Y = +4px  
Frame 3: Y = +6px or +7px (lowest point)
Frame 4: Y = +4px (same as frame 2)
Frame 5: Y = +2px (same as frame 1)
Loop back to frame 0
```

This creates a "bouncing" effect - the small face bobs up and down rhythmically.

## Static Elements

- Large left face: COMPLETELY STATIC (no animation)
- Background: Static
- Only the small right face animates

## SVG Implementation Strategy

Since this is a double-width smiley (29×15), we need to create an SVG that's 32×16 to match the double-width format.

Two approaches:
1. Create a 32×16 SVG with both faces
2. Create two separate 16×16 SVGs (one static large face, one animated small face)

Given the established pattern, approach #1 (single 32×16 SVG) makes more sense.

Structure:
- Large left face (static) positioned on left half
- Small right face (animated) positioned on right half with vertical translation animation
