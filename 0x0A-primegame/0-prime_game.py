def sieve_of_eratosthenes(max_num):
    """Precompute prime numbers
    up to max_num using the Sieve of Eratosthenes."""
    sieve = [True] * (max_num + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes

    for start in range(2, int(max_num**0.5) + 1):
        if sieve[start]:
            for multiple in range(start * start, max_num + 1, start):
                sieve[multiple] = False

    return sieve


def count_prime_moves(n, primes):
    """Count the number of prime moves possible for a given n."""
    moves = 0
    visited = [False] * (n + 1)

    for i in range(2, n + 1):
        if primes[i] and not visited[i]:
            moves += 1
            for multiple in range(i, n + 1, i):
                visited[multiple] = True

    return moves


def isWinner(x, nums):
    """Determine the winner of the Prime Game."""
    if x < 1 or not nums:
        return None

    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_moves = count_prime_moves(n, primes)
        if prime_moves % 2 == 1:  # If odd, Maria wins
            maria_wins += 1
        else:  # If even, Ben wins
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
