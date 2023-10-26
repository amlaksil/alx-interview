#!/usr/bin/python3
"""
This module contains a function called validUTF8 that
checks if a given data represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Checks if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list of int): The data set represented by a list of integers.

    Returns:
        bool: True if data is a valid UTF-8 encoding, False otherwise.
    """

    num_bytes = 0

    for num in data:
        if num_bytes == 0:
            # Checking the first few bits to determine the number
            # of bytes for the character
            if (num >> 5) & 0b111 == 0b110:
                num_bytes = 1
            elif (num >> 4) & 0b1111 == 0b1110:
                num_bytes = 2
            elif (num >> 3) & 0b11111 == 0b11110:
                num_bytes = 3
            elif (num >> 7) & 0b1 != 0:
                # If the first bit is 1, it's not a valid UTF-8 character
                return False
        else:
            # Checking if the first 2 bits are '10' for continuation bytes
            if (num >> 6) & 0b11 != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 0
