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


def sum_of_integers_not_sum_of_abundant_pairs():
    sum_of_non_abundant_pairs = 0
    abundant_numbers = []

    for x in range(28124):
        if not is_sum_of_abundant_numbers(x, abundant_numbers):
            sum_of_non_abundant_pairs += x

    return sum_of_non_abundant_pairs


def is_sum_of_abundant_numbers(number, abundant_numbers):
    while not abundant_numbers or abundant_numbers[-1] < number:
        find_next_abundant_number(abundant_numbers)

    low_index = 0
    high_index = len(abundant_numbers) - 1
    while low_index <= high_index:
        if abundant_numbers[low_index] + abundant_numbers[high_index] > number:
            high_index -= 1
        elif abundant_numbers[low_index] + abundant_numbers[high_index] < number:
            low_index += 1
        else:
            return True

    return False


def find_next_abundant_number(abundant_numbers):
    number = abundant_numbers[-1] if abundant_numbers else 0
    while True:
        number += 1
        if sum(proper_divisors_of(number)) > number:
            abundant_numbers.append(number)
            break


def proper_divisors_of(number):
    if number > 1:
        yield 1
    for i in range(2, int(number ** 0.5) + 1):
        if not number % i:
            yield i
            if i * i != number:
                yield number // i


def main():
    solution = sum_of_integers_not_sum_of_abundant_pairs()

    print('Solution: %s.\nExecution time: %s seconds.' % (solution, time.time() - start_time))


if __name__ == '__main__':
    main()
