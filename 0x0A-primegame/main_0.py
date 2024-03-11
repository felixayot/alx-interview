#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner


print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
print("Winner: {}".format(isWinner(2, [2, 1])))
print("Winner: {}".format(isWinner(
    3, [17, 13, 11, 10, 12, 19, 20, 22, 21, 23, 24,
        25, 26, 27, 28, 29, 30, 31, 32, 33])))
