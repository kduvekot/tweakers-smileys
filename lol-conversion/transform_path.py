#!/usr/bin/env python3
"""
Apply SVG transforms to path coordinates.
Transform sequence: translate(0, 11) scale(1, 0.4) skewX(10deg)
"""
import re
import math

def parse_path(d):
    """Simple path parser for basic commands"""
    # This is a simplified parser - handles M, v, a commands
    return d

def skew_x_matrix(degrees):
    """Create skewX transform matrix"""
    angle_rad = math.radians(degrees)
    tan_angle = math.tan(angle_rad)
    return [[1, tan_angle, 0],
            [0, 1, 0],
            [0, 0, 1]]

def scale_matrix(sx, sy):
    """Create scale transform matrix"""
    return [[sx, 0, 0],
            [0, sy, 0],
            [0, 0, 1]]

def translate_matrix(tx, ty):
    """Create translate transform matrix"""
    return [[1, 0, tx],
            [0, 1, ty],
            [0, 0, 1]]

def multiply_matrices(m1, m2):
    """Multiply two 3x3 matrices"""
    result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                result[i][j] += m1[i][k] * m2[k][j]
    return result

def transform_point(x, y, matrix):
    """Apply transformation matrix to a point"""
    new_x = matrix[0][0] * x + matrix[0][1] * y + matrix[0][2]
    new_y = matrix[1][0] * x + matrix[1][1] * y + matrix[1][2]
    return new_x, new_y

def transform_path_simple(d, matrix):
    """Transform path - handle common patterns"""
    # This transforms absolute coordinates in the path
    # Handle M, v, V commands

    # Find all coordinate pairs (numbers)
    def transform_coords(match):
        x = float(match.group(1))
        y = float(match.group(2))
        new_x, new_y = transform_point(x, y, matrix)
        return f"{new_x:.3f} {new_y:.3f}"

    # Simple pattern for coordinate pairs
    # This is very simplified and won't handle all SVG path cases correctly
    result = d
    return result

# Combine transforms: translate(0,11) * scale(1,0.4) * skewX(10deg)
# Note: SVG transforms are applied right-to-left
translate_m = translate_matrix(0, 11)
scale_m = scale_matrix(1, 0.4)
skew_m = skew_x_matrix(10)

# Multiply: translate * scale * skew (applied right to left)
combined = multiply_matrices(multiply_matrices(translate_m, scale_m), skew_m)

print("Combined transformation matrix:")
print(f"[{combined[0][0]:.6f}, {combined[0][1]:.6f}, {combined[0][2]:.6f}]")
print(f"[{combined[1][0]:.6f}, {combined[1][1]:.6f}, {combined[1][2]:.6f}]")
print(f"[{combined[2][0]:.6f}, {combined[2][1]:.6f}, {combined[2][2]:.6f}]")
print()

# Test with a few key points from the hand path
test_points = [
    (8.125, 5.375),  # Start of first path
    (1.875, 3.655),  # Another point
    (4.125, 6.938),  # Bottom of hand
]

print("Sample point transformations:")
for x, y in test_points:
    new_x, new_y = transform_point(x, y, combined)
    print(f"  ({x:.3f}, {y:.3f}) -> ({new_x:.3f}, {new_y:.3f})")
