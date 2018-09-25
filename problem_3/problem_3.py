"""
Author: Berdal, Ole
Created: 25.09.2018
Version: Python 3.7.0

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""
import time
start_time = time.time()

def find_primes(number, start=2):
    prime_factors = []
    for x in range(start, number + 1):
        if not number % x:
            while not number % x:
                number //= x
            prime_factors.append(x)
            return prime_factors + ([] if number == 1 else find_primes(number, x + 1))

solution = max(find_primes(600851475143))

print("Solution: %s.\nExecution time: %s seconds." % (solution, time.time() - start_time))