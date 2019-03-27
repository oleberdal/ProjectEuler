"""
Author: Berdal, Ole
Created: 25.09.2018
Edited: 27.03.2019
Version: Python 3.6.7

https://projecteuler.net/problem=3:
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""
import time
start_time = time.time()


def find_prime_factors(number, start=3):
    for divisor in range(2 if not number % 2 else start, int(number**0.5) + 1, 1 + number % 2):
        if not number % divisor:
            while not number % divisor:
                number //= divisor
            return [divisor] + find_prime_factors(number, divisor + divisor % 2 + 1)

    return [number] if number > 1 else []


def main():
    solution = max(find_prime_factors(number=600851475143))

    print('Solution: %s.\nExecution time: %s seconds.' % (solution, time.time() - start_time))


if __name__ == '__main__':
    main()
