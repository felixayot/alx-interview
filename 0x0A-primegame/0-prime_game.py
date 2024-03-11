#!/usr/bin/python3
"""Module for Prime Game Winner Implementation."""


def is_prime(n):
    """Checks if a given number n is a prime number."""
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            return False
    return True


def calculate_primes(n, primes):
    """Calculate all primes."""
    top_prime = primes[-1]
    if n > top_prime:
        for i in range(top_prime + 1, n + 1):
            if is_prime(i):
                primes.append(i)
            else:
                primes.append(0)


def isWinner(x, nums):
    """Determine the winner of the prime game."""
    players_wins = {"Maria": 0, "Ben": 0}
    primes = [0, 0, 2]
    calculate_primes(max(nums), primes)

    for round in range(x):
        sum_options = sum((i != 0 and i <= nums[round])
                          for i in primes[:nums[round] + 1])
        if (sum_options % 2):
            winner = "Maria"
        else:
            winner = "Ben"
        if winner:
            players_wins[winner] += 1

    if players_wins["Maria"] > players_wins["Ben"]:
        return "Maria"
    elif players_wins["Ben"] > players_wins["Maria"]:
        return "Ben"

    return None
