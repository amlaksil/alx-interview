#!/usr/bin/python3

"""
This module contains a function called `makeChange` that calculates
the minimum number of coins needed to make a specific total using
a given set of coin denominations.
"""


def makeChange(coins, total):
    """
    Calculates the minimum number of coins needed to make a specific
    total using a given set of coin denominations.

    Args:
        coins (list): A list of coin denominations.
        total (int): The target total to be achieved.

    Returns:
        int: The minimum number of coins needed to make the total.
        If it's not possible to make the exact total with the given
        coins, returns -1.

    Raises:
        None

    Example:
        >>> coins = [1, 5, 10, 25]
        >>> total = 30
        >>> makeChange(coins, total)
        2
    """
    # Store the minimum number of coins needed for each amount from 0 to total
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            # Check if using the current coin leads to a smaller number ofcoins
            if coin <= i:
                min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)

    if min_coins[total] == float('inf'):
        # Cannot reach the exact total with the given coins
        return -1
    return min_coins[total]
