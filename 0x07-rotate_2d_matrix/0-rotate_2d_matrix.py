#!/usr/bin/python3
"""Module that
    Given an n x n 2D matrix, rotate it 90 degrees clockwise.
    Prototype: def rotate_2d_matrix(matrix):
    Do not return anything. The matrix must be edited in-place.
    You can assume the matrix will have 2 dimensions and will not be empty."""


def rotate_2d_matrix(matrix):
    """Function recives a matrix and rotates it 90 degrees clockwise."""
    n = len(matrix)
    rotated = [[matrix[n-1-j][i] for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            matrix[i][j] = rotated[i][j]
