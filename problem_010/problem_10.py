"""
Author: Berdal, Ole
Created: 28.09.2018
Edited: 01.10.2018
Version: Python 3.7.0

https://projecteuler.net/problem=10:
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
import time
start_time = time.time()


def find_prime_numbers_below(below):
    total = 2
    sieve = [True] * below
    for p in range(3, below, 2):
        if sieve[p]:
            total += p
            for i in range(p * p, below, p * 2):
                sieve[i] = False

    return total


def main():
    solution = find_prime_numbers_below(2000000)

    print('Solution: %s.\nExecution time: %s seconds.' % (solution, time.time() - start_time))


if __name__ == '__main__':
    main()
