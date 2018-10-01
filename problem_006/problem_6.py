"""
Author: Berdal, Ole
Created: 26.09.2018
Edited: 28.09.2018
Version: Python 3.7.0

https://projecteuler.net/problem=6:
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
import time
start_time = time.time()


def difference_between(first):
    return abs(sum_of_numbers(first)**2 - sum_of_squared_numbers(first))


def sum_of_numbers(to):
    return to * (to + 1) / 2


def sum_of_squared_numbers(to):
    total = 0
    for x in range(1, to + 1):
        total += x * (2 * (to - x) + 1)

    return total


def main():
    solution = int(difference_between(100))

    print('Solution: %s.\nExecution time: %s seconds.' % (solution, time.time() - start_time))


if __name__ == '__main__':
    main()