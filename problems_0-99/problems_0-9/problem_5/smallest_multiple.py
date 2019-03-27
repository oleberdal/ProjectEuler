"""
Author: Berdal, Ole
Created: 26.09.2018
Edited: 27.03.2019
Version: Python 3.6.7

https://projecteuler.net/problem=5:
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
import time
start_time = time.time()


def smallest_number_divisible_by(divisors):
    prime_factors = {}
    for divisor in divisors:
        for prime, n in reduce_to_primes(number=divisor).items():
            prime_factors[prime] = max(prime_factors.get(prime, 0), n)

    divisible_number = 1
    for prime, exponent in prime_factors.items():
        divisible_number *= prime**exponent

    return divisible_number


def reduce_to_primes(number, start=3):
    prime_factors = {}
    for divisor in range(2 if not number % 2 else start, int(number ** 0.5) + 1, 1 + number % 2):
        if not number % divisor:
            while not number % divisor:
                number //= divisor
                prime_factors[divisor] = prime_factors.get(divisor, 0) + 1
            prime_factors.update(reduce_to_primes(number=number, start=divisor + divisor % 2 + 1))
            return prime_factors
    return {number: 1} if number > 1 else {}


def main():
    solution = smallest_number_divisible_by(divisors=range(2, 21))

    print('Solution: %s.\nExecution time: %s seconds.' % (solution, time.time() - start_time))


if __name__ == '__main__':
    main()
