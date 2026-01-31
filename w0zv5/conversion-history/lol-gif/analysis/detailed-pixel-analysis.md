# Detailed Pixel Analysis - LoL Smiley

## Canvas Structure (29×15 pixels)

The GIF contains:
1. **Left section (0-15px)**: Large face with left arm
2. **Right section (16-28px)**: Small bouncing face

## Large Face (Left Side)
- Position: Approximately centered at (8, 7.5) in left 16px
- Features:
  - Squinting/laughing eyes (horizontal lines at Y≈5-6)
  - Wide open mouth/grin (curved line at Y≈9-11)
  - Yellow gradient fill
  - Dark outline

## Small Face (Right Side)  
- Much smaller than left face
- Bounces vertically frame by frame
- Has round eyes and small smile
- Positioned in upper right area

## Left Arm/Hand
- Yellow elliptical shape
- Positioned at lower left (approximately X=2-3, Y=11-13)
- Static (no animation)

## Frame-by-Frame Small Face Position

Examining the cropped small face images:

**Frame 0**: Small face at highest/starting position
**Frame 1**: Moved down ~2px  
**Frame 2**: Moved down ~4px from frame 0
**Frame 3**: Moved down ~6px from frame 0 (lowest point)
**Frame 4**: Back to ~4px down (same as frame 2)
**Frame 5**: Back to ~2px down (same as frame 1)

## SVG Scaling Strategy

Original: 29×15 pixels
SVG Target: 32×16 pixels (double-width standard)

Scale factor: ~1.1x in both dimensions
- This allows for proper positioning in standard grid
- Maintains aspect ratio
