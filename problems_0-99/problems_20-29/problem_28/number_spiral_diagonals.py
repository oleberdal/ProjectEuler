"""
Author: Berdal, Ole
Created: 11.03.2019
Version: Python 3.6.8

https://projecteuler.net/problem=28:
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""
import time
start_time = time.time()


def sum_of_diagonal_in_spiral(size):
    total = last = 1
    for depth in range(2, size + 1, 2):
        total += 4 * last + 10 * depth
        last += 4 * depth

    return total


def main():
    solution = sum_of_diagonal_in_spiral(size=1001)

    print('Solution: %s.\nExecution time: %s seconds.' % (solution, time.time() - start_time))


if __name__ == '__main__':
    main()
