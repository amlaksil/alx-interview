#!/usr/bin/python3
"""
Module: lockboxes

This module provides a function for determining if all the
boxes can be opened.
"""


def canUnlockAll(boxes):
    """Checks if it is possible to unlock all boxes in a given set.

    This function determines whether it is possible to unlock all
    boxes in the set, given that each box may contain keys to other
    boxes. The function utilizes a depth-first search (DFS) approach
    to explore the boxes and their corresponding keys.

    Args:
        boxes (list): A list of lists representing the boxes and their
    corresponding keys. Each box is numbered sequentially from 0 to
    n - 1, where n is the total number of boxes. Each inner list contains
    positive integer keys that can open other boxes.
    Returns:
        bool: True if all boxes can be opened, False otherwise.

    Notes:
        - A key with the same number as a box opens that box.
        - The first box boxes[0] is assumed to be unlocked.
        - Keys that do not have corresponding boxes are allowed.

    Examples:
        >>> boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
        >>> canUnlockAll(boxes)
        True

        >>> boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
        >>> canUnlockAll(boxes)
        False
    """
    num_boxes = len(boxes)
    visited = [False] * num_boxes  # List to track visited/unlocked boxes
    visited[0] = True

    stack = [0]  # Stack for depth-first search traversal

    while stack:
        box = stack.pop()
        for key in boxes[box]:
            if key < num_boxes and not visited[key]:
                # If the key is within the valid range and
                # the corresponding box is not visited
                visited[key] = True
                stack.append(key)

    return all(visited)
