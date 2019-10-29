"""
Author: Berdal, Ole
Created: 26.09.2018
Edited: 29.10.2019
Version: Python 3.7.4

https://projecteuler.net/problem=6:
The sum of the squares of the first ten natural numbers is,

1² + 2² + ... + 10² = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)² = 55² = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
import time
start_time = time.time()


def difference_between_square_of_sum_and_sum_of_squares(until):
    return (until * (until + 1) // 2)**2 - sum(tuple(n**2 for n in range(1, until + 1)))


def main():
    solution = difference_between_square_of_sum_and_sum_of_squares(until=10**2)

    print('Solution: %s.\nExecution time: %s seconds.' % (solution, time.time() - start_time))


if __name__ == '__main__':
    main()
