"""
Author: Berdal, Ole
Created: 06.02.2019
Version: Python 3.6.7

https://projecteuler.net/problem=21:
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
import time
start_time = time.time()


def sum_of_amicable_numbers_below(below):
    proper_divisors = [(1, 1)]

    for n in range(2, below):
        proper_divisors.append((n, sum(proper_divisors_of(n))))

    total = 0
    while len(proper_divisors) > 0:
        search = proper_divisors.pop(0)
        compliment = search[::-1]
        if search[1] >= below:
            if sum(proper_divisors_of(search[1])) == search[0]:
                total += search[0]
        elif compliment in proper_divisors:
                index = proper_divisors.index(compliment)
                total += search[0] + proper_divisors[index][0]
                proper_divisors.pop(index)

    return total


def proper_divisors_of(number):
    yield 1
    for i in range(2, int(number ** 0.5 + 1)):
        if not number % i:
            yield i
            if i * i != number:
                yield number // i


def main():
    solution = sum_of_amicable_numbers_below(10000)

    print('Solution: %s.\nExecution time: %s seconds.' % (solution, time.time() - start_time))


if __name__ == '__main__':
    main()
