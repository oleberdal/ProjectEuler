"""
Author: Berdal, Ole
Created: 26.09.2018
Edited: 01.10.2018
Version: Python 3.7.0

https://projecteuler.net/problem=5:
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
import time
start_time = time.time()


def smallest_divisible_number(primes):
    numbers = []
    for x in range(2, primes + 1):
        numbers.append(reduce_to_primes(number=x))

    prime_factors = {}
    for primes in numbers:
        for prime, n in primes.items():
            if prime_factors.get(prime, 0) < n:
                prime_factors[prime] = n

    divisible_number = 1
    for prime, x in prime_factors.items():
        divisible_number *= prime ** x

    return divisible_number


def reduce_to_primes(number, start=3):
    start = 2 if not number % 2 else start
    bound = int(number ** 0.5) + 1
    step = 1 + number % 2
    prime_factors = {}
    for x in range(start, bound, step):
        if not number % x:
            while not number % x:
                number //= x
                prime_factors[x] = prime_factors.get(x, 0) + 1
            prime_factors.update(reduce_to_primes(number=number, start=x + 1 + x % 2))
            return prime_factors
    return {number: 1} if number > 1 else {}


def main():
    solution = smallest_divisible_number(primes=20)

    print('Solution: %s.\nExecution time: %s seconds.' % (solution, time.time() - start_time))


if __name__ == '__main__':
    main()
