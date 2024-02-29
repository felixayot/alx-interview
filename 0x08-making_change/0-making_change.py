#!/usr/bin/python3
"""makeChange module."""


def makeChange(coins, total):
    """Given a pile of coins of different values,
    determine the fewest number
    of coins needed to meet a given amount total.
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    n = 0
    for coin in coins:
        if total <= 0:
            break
        n += total // coin
        total %= coin
    return n if total == 0 else -1
