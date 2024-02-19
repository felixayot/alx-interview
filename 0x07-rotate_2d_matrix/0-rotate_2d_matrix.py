#!/usr/bin/python3
"""Script to rotate a `n x n` 2D matrix."""
import math


def rotate_2d_matrix(matrix):
    """Rotates a 2D matrix 90 degrees clockwise
       using In-place operation."""
    n = len(matrix)
    for i in range(math.floor(n / 2)):
        for j in range(i, n - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
            matrix[j][n - 1 - i] = temp
