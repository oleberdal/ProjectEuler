"""
Author: Berdal, Ole
Created: 26.09.2018
Edited: 29.10.2019
Version: Python 3.7.4

https://projecteuler.net/problem=7:
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6ᵗʰ prime is 13.

What is the 10 001ᵗʰ prime number?
"""
import time
start_time = time.time()


def find_prime_number(n):
    primes, number = [2], 3
    while len(primes) < n:
        if is_prime(number=number, primes=primes):
            primes.append(number)
        number += 2

    return primes[n - 1]


def is_prime(number, primes):
    bound, i = int(number**0.5), 0
    while primes[i] <= bound:
        if not number % primes[i]:
            return False
        i += 1

    return True


def main():
    solution = find_prime_number(n=10001)

    print('Solution: %s.\nExecution time: %s seconds.' % (solution, time.time() - start_time))


if __name__ == '__main__':
    main()
