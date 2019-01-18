"""
Author: Berdal, Ole
Created: 25.09.2018
Edited: 01.10.2018
Version: Python 3.7.0

https://projecteuler.net/problem=3:
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""
import time
start_time = time.time()


def find_prime_factors(n, start=3):
    start = 2 if not n % 2 else start
    bound = int(n**0.5) + 1
    step = 1 if not n % 2 else 2
    prime_factors = []
    for x in range(start, bound, step):
        if not n % x:
            while not n % x:
                n //= x
            prime_factors.append(x)
            return prime_factors + find_prime_factors(n, x + 1 + x % 2)
    else:
        return [n] if n > 1 else []


def main():
    solution = max(find_prime_factors(600851475143))

    print('Solution: %s.\nExecution time: %s seconds.' % (solution, time.time() - start_time))


if __name__ == '__main__':
    main()