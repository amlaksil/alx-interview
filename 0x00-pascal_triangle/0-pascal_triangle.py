#!/usr/bin/python3

"""This module contains a function called pascal_triangle
which generates pascal's triangle up to the specified number
of rows
"""


def pascal_triangle(n):
    """Generates Pascal's triangle up to the specified number of rows.
    Args:
        n (int): The number of rows in Pascal's triangle.
    Returns:
        list: A list of lists representing Pascal's triangle.
        Each inner list represents a row of Pascal's triangle,
        containing the entries.
    Raises:
        None
    Example:
        >>> pascal_triangle(5)
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                # Calculate the entry using the combinatorial formula
                entry = triangle[i - 1][j - 1] + triangle[i - 1][j]
                row.append(entry)
        triangle.append(row)
    return triangle
