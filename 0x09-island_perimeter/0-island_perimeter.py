#!/usr/bin/python3
"""0-island_perimeter.py module for island_perimeter function."""


def island_perimeter(grid):
    """Returns the perimeter of the island described in grid:
        0 represents a water zone
        1 represents a land zone
        One cell is a square with side length 1
        Grid cells are connected horizontally/vertically (not diagonally).
        Grid is rectangular, width and height don’t exceed 100.
        Grid is completely surrounded by water, and there is one island
        (or nothing).
        The island doesn’t have “lakes” (water inside that isn’t
        connected to the water around the island).
    Args:
     grid(list): list of list of integers.
    """
    width = len(grid[0])
    height = len(grid)
    edges = 0
    size = 0

    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:
                size += 1
                if (j > 0 and grid[i][j - 1] == 1):
                    edges += 1
                if (i > 0 and grid[i - 1][j] == 1):
                    edges += 1
    return size * 4 - edges * 2
