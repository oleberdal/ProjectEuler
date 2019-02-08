"""
Author: Berdal, Ole
Created: 08.02.2019
Version: Python 3.6.7

https://projecteuler.net/problem=23:
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""
import time
start_time = time.time()


def find_sum_of_non_abundant_pairs():
    abundants, total = set(), 0
    for number in range(1, 20612):
        if sum(divisors(number)) > number:
            abundants.add(number)
        if not any(number - abundant in abundants for abundant in abundants):
            total += number

    return total


def divisors(number):
    if number > 1:
        yield 1
    for divisor in range(2, int(number ** 0.5) + 1):
        if not number % divisor:
            yield divisor
            if divisor * divisor != number:
                yield number // divisor


def main():
    solution = find_sum_of_non_abundant_pairs()

    print('Solution: %s.\nExecution time: %s seconds.' % (solution, time.time() - start_time))


if __name__ == '__main__':
    main()
