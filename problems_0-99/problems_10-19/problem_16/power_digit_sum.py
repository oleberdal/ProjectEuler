"""
Author: Berdal, Ole
Created: 05.02.2019
Edited: 03.10.2019
Version: Python 3.7.4

https://projecteuler.net/problem=16:
2¹⁵ = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2¹⁰⁰⁰?
"""
import time
start_time = time.time()


def sum_of_digits_of_number(number):
    return sum([int(d) for d in str(number)])


def main():
    solution = sum_of_digits_of_number(number=2**10**3)

    print('Solution: %s.\nExecution time: %s seconds.' % (solution, time.time() - start_time))


if __name__ == '__main__':
    main()
