"""
Author: Berdal, Ole
Created: 28.09.2018
Edited: 29.10.2019
Version: Python 3.7.4

https://projecteuler.net/problem=10:
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
import time
start_time = time.time()


def sum_of_prime_numbers_below(below):
    total, sieve = 2, [True] * below
    for prime in range(3, below, 2):
        if sieve[prime]:
            total += prime
            for i in range(prime ** 2, below, prime * 2):
                sieve[i] = False

    return total


def main():
    solution = sum_of_prime_numbers_below(below=2 * 10 ** 6)

    print('Solution: %s.\nExecution time: %s seconds.' % (solution, time.time() - start_time))


if __name__ == '__main__':
    main()
