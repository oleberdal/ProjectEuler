"""
Author: Berdal, Ole
Created: 25.09.2018
Edited: 28.09.2018
Version: Python 3.7.0

https://projecteuler.net/problem=3:
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""
import time
start_time = time.time()


def find_primes(n, start=2):
    prime_factors = []
    for x in range(start, n + 1):
        if not n % x:
            while not n % x:
                n //= x
            prime_factors.append(x)
            return prime_factors + ([] if n == 1 else find_primes(n, x + 1))


def main():
    solution = max(find_primes(600851475143))

    print('Solution: %s.\nExecution time: %s seconds.' % (solution, time.time() - start_time))


if __name__ == '__main__':
    main()