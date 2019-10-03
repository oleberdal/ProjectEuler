"""
Author: Berdal, Ole
Created: 25.09.2018
Edited: 03.10.2019
Version: Python 3.7.4

https://projecteuler.net/problem=1:
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
import time
start_time = time.time()


def sum_of_multiples(below, multiples):
    total = 0
    for number in range(below):
        for multiple in multiples:
            if not number % multiple:
                total += number
                break

    return total


def main():
    solution = sum_of_multiples(below=10**3, multiples=[3, 5])

    print('Solution: %s.\nExecution time: %s seconds.' % (solution, time.time() - start_time))


if __name__ == '__main__':
    main()
