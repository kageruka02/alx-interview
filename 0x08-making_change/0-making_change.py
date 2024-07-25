#!/usr/bin/python3
"Making change"


def makeChange(coins, total):
    "Making change"
    if total <= 0:
        return 0

    # Initialize dp array with infinity for all values except dp[0]
    dp = [float("inf")] * (total + 1)
    dp[0] = 0

    # Update dp array using the coin values
    for coin in coins:
        for amount in range(coin, total + 1):
            if dp[amount - coin] != float("inf"):
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # Return the result
    return dp[total] if dp[total] != float("inf") else -1
