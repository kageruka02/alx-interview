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


# Test cases
if __name__ == "__main__":
    print(makeChange([1, 2, 25], 37))  # Expected output: 7
    print(makeChange([1256, 54, 48, 16, 102], 1453))  # Expected output: -1
