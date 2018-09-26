"""
Author: Berdal, Ole
Created: 26.09.2018
Version: Python 3.7.0

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
import time
start_time = time.time()


def is_prime(n, primes):
    for p in primes:
        if not n % p:
            return False
    return True


def find_prime_number(n):
    primes = []

    c = 2
    while len(primes) < n:
        if is_prime(c, primes):
            primes.append(c)
        c += 1

    return primes[-1]


def main():
    solution = find_prime_number(10001)

    print('Solution: %s.\nExecution time: %s seconds.' % (solution, time.time() - start_time))


if __name__ == '__main__':
    main()