"""
Author: Berdal, Ole
Created: 26.09.2018
Version: Python 3.7.0

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
import time
start_time = time.time()


def reduce_to_primes(n, start=2):
    prime_factors = []

    for x in range(start, n + 1):
        if not n % x:
            n //= x
            prime_factors.append([x, 1])
            while not n % x:
                n //= x
                prime_factors[-1][1] += 1
            return prime_factors + ([] if n == 1 else reduce_to_primes(n, x + 1))


def smallest_divisible_number(n):
    numbers = []
    for x in range(2, n + 1):
        numbers.append(reduce_to_primes(x))

    prime_factors = {}
    for n in numbers:
        for p in n:
            if p[0] not in prime_factors or prime_factors[p[0]] < p[1]:
                prime_factors[p[0]] = p[1]

    number = 1
    for p, x in prime_factors.items():
        number *= p**x

    return number


def main():
    solution = smallest_divisible_number(20)

    print('Solution: %s.\nExecution time: %s seconds.' % (solution, time.time() - start_time))


if __name__ == '__main__':
    main()