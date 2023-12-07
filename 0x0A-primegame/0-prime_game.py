#!/usr/bin/python3

"""
This module contains a function called isWinner which
helps us to determine the winner of the game.Description for the game:
Maria and Ben are playing a game. Given a set of consecutive integers starting
from 1 up to and including n, they take turns choosing a prime number from the
set and removing that number and its multiples from the set. The player that
cannot make a move loses the game. Assuming Maria always goes first and both
players play optimally.
"""


def isWinner(x, nums):
    """
    Determine the winner of the prime game for each round.

    Args:
        x (int): The number of rounds. (Unused)
        nums (list): A list of integers representing n for each round.

    Returns:
        str or None: The name of the player (Maria or Ben) that won the most
        rounds, or None if the winner cannot be determined.
    """
    if not nums or x < 1:
        return None
    max_num = max(nums)

    my_filter = [True for _ in range(max(max_num + 1, 2))]
    for i in range(2, int(pow(max_num, 0.5)) + 1):
        if not my_filter[i]:
            continue
        for j in range(i * i, max_num + 1, i):
            my_filter[j] = False
    my_filter[0] = my_filter[1] = False
    y = 0
    for i in range(len(my_filter)):
        if my_filter[i]:
            y += 1
        my_filter[i] = y
    player1 = 0
    for x in nums:
        player1 += my_filter[x] % 2 == 1
    if player1 * 2 == len(nums):
        return None
    if player1 * 2 > len(nums):
        return "Maria"
    return "Ben"
