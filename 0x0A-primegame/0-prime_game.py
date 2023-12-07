#!/usr/bin/python3
"""
This module contains functions needed to determine the winner of the game.
Description for the game: Maria and Ben are playing a game. Given a set of
consecutive integers starting from 1 up to and including n, they take turns
choosing a prime number from the set and removing that number and its multiples
from the set. The player that cannot make a move loses the game. Assuming Maria
always goes first and both players play optimally.
"""


def is_prime(num):
    """
    Check if a number is prime.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, num + 1):
        if num % i == 0:
            return False
    return True


def isWinner(_, nums):
    """
    Determine the winner of the prime game for each round.

    Args:
        _ (int): The number of rounds. (Unused)
        nums (list): A list of integers representing n for each round.

    Returns:
        str or None: The name of the player (Maria or Ben) that won the most
        rounds, or None if the winner cannot be determined.
    """
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = [num for num in range(2, n + 1) if is_prime(num)]

        if len(primes) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None
