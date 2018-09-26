"""
Author: Berdal, Ole
Created: 26.09.2018
Version: Python 3.7.0

The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
import time
start_time = time.time()


def list_of_squared_numbers(to):
    return [x**2 for x in range(to + 1)]


def sum_of_numbers(to):
    return to * (to + 1) / 2


def main():
    solution = abs(sum_of_numbers(100)**2 - sum(list_of_squared_numbers(100)))

    print('Solution: %s.\nExecution time: %s seconds.' % (solution, time.time() - start_time))


if __name__ == '__main__':
    main()