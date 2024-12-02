#!/usr/bin/python3
"""
Given a pile of coins of different values,
determine the fewest number of coins needed to meet a given amount total.
"""


def makeChange(coins, total):
    if total <= 0:
        return 0
    dp_array = [float('inf')] * (total + 1)
    dp_array[0] = 0

    for coin in coins:
        for x in range(coin, total + 1):
            dp_array[x] = min(dp_array[x], dp_array[x - coin] + 1)

    return dp_array[total] if dp_array[total] != float('inf') else -1
