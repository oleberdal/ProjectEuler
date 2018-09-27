"""
Author: Berdal, Ole
Created: 26.09.2018
Edited: 28.09.2018
Version: Python 3.7.0

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
import time
start_time = time.time()


def is_prime(n, primes):
    bound = int(n**0.5) + 1
    i = 0
    while primes[i] <= bound:
        if not n % primes[i]:
            return False
        i += 1

    return True


def find_prime_number(n):
    primes = [3, 5]
    bound = n - 1
    c = 7
    while len(primes) < bound:
        if is_prime(c, primes):
            primes.append(c)
        c += 2

    return primes[-1]


def main():
    solution = find_prime_number(10001)

    print('Solution: %s.\nExecution time: %s seconds.' % (solution, time.time() - start_time))


if __name__ == '__main__':
    main()