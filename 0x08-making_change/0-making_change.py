#!/usr/bin/python3
"""Module determines determine the fewest number of coins
    needed to meet a given amount total."""


def makeChange(coins, total):
    """Function returns the fewest number of coins needed to
    meet a given amount total greedy."""
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    amount = 0
    for coin in coins:
        if total == 0:
            break
        amount += total // coin
        total -= (total // coin) * coin
    return amount if total == 0 else -1
