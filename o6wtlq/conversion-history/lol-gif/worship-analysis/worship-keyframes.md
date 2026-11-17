# Worship SVG Animation Keyframes Analysis

## Animation Duration
Total: 2s (2000ms) linear infinite

## Face Animation (a1)
```css
@keyframes a1 {
  0%, 65%, to { transform: translate(0,0) scale(1) }      /* Normal position */
  15%, 50%     { transform: translate(0,8px) scale(1,.5) } /* Bowing down */
}
```

**States:**
- 0% (0ms): Normal - translate(0,0) scale(1)
- 15% (300ms): Going down - translate(0,8px) scale(1,.5)
- 50% (1000ms): Down (held) - translate(0,8px) scale(1,.5)
- 65% (1300ms): Back up - translate(0,0) scale(1)
- 100% (2000ms): Normal - translate(0,0) scale(1)

## Both Hands Animation (a2)
```css
@keyframes a2 {
  0%       { transform: translate(0) }                    /* Up */
  15%, 50% { transform: translate(0,11px) scale(1,.4) }  /* Down */
  65%, to  { transform: translate(0) scale(1) }          /* Back up */
}
```

**States:**
- 0% (0ms): Up - translate(0)
- 15% (300ms): Going down - translate(0,11px) scale(1,.4)
- 50% (1000ms): Down (held) - translate(0,11px) scale(1,.4)
- 65% (1300ms): Back up - translate(0) scale(1)
- 100% (2000ms): Up - translate(0) scale(1)

## Left Hand Additional (a2l)
```css
@keyframes a2l {
  0%, 65%, to { transform: skewX(0) }
  15%, 50%    { transform: skewX(10deg) }
}
```

## Right Hand Additional (a2r)
```css
@keyframes a2r {
  0%, 65%, to { transform: skewX(0) }
  15%, 50%    { transform: skewX(-10deg) }
}
```

## Key Transition Points

For analysis, we should capture these 5 states:

1. **State 0% (0ms)** - Everything normal/up
2. **State 15% (300ms)** - Transitioning down
3. **State 50% (1000ms)** - Fully down (held position)
4. **State 65% (1300ms)** - Transitioning back up
5. **State 100% (2000ms)** - Back to normal

Then create transitions:
- 0% → 15% (going down)
- 15% → 50% (settling into down position)
- 50% → 65% (starting to rise)
- 65% → 100% (returning to normal)
- 100% → 0% (loop)
