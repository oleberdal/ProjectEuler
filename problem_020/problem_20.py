"""
Author: Berdal, Ole
Created: 06.02.2019
Version: Python 3.6.7

https://projecteuler.net/problem=20:
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""
import time
start_time = time.time()


def sum_of_digits_in_factorial(number):
    return sum(map(int, str(factorial(number))))


def factorial(n):
    return n * factorial(n - 1) if n > 1 else 1


def main():
    solution = sum_of_digits_in_factorial(100)

    print('Solution: %s.\nExecution time: %s seconds.' % (solution, time.time() - start_time))


if __name__ == '__main__':
    main()
