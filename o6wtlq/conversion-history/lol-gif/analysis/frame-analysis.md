# Detailed Frame Analysis of LoL GIF

## Frame Dimensions
- Full GIF: 29×15 pixels
- Center face region: 15×15 pixels (extracted from X=7 to X=22)
- Left hand region: 7×15 pixels (X=0 to X=7)
- Right hand region: 7×15 pixels (X=22 to X=29)

## Center Face Analysis

### MD5 Hashes (non-mega):
- Frame 0: f66b6d022f4067c09d14e1fef97918aa
- Frame 1: a7a322d637bd02e5580b9f4c79223ff2 ← DIFFERENT from frame 0
- Frame 2: a7a322d637bd02e5580b9f4c79223ff2 ← Same as frame 1
- Frame 3: 8209cd87b4787039732be4061aef3c33 ← DIFFERENT
- Frame 4: 8209cd87b4787039732be4061aef3c33 ← Same as frame 3
- Frame 5: 8209cd87b4787039732be4061aef3c33 ← Same as frame 3

### MD5 Hashes (mega - 2000% scaled):
- Frames 0,1: 7e60776c378669a51d58f198a72b1dfb
- Frames 2,3,4,5: 2b5b1bf1f3a7322df17215560f5c495c

### Conclusion so far:
The center face is NOT completely static! It changes between frames.
- Pattern: Frame 0 unique, then Frame 1-2 are one state, Frame 3-5 are another state
- Or possibly: Frames 0-1 are one state (when scaled), Frames 2-5 are another state

## Left Hand Analysis

MD5 unique count: 5 different hashes out of 6 frames
This means the left hand is also CHANGING across frames!

## Right Hand Analysis

This is the obvious one - it's clearly bouncing up and down.

## Key Question from User:
**"Is the face circle fully visible at all times?"**

Looking at the center face frames, I need to check if the top or bottom of the circle gets cut off.
