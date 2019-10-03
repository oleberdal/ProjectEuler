"""
Author: Berdal, Ole
Created: 02.03.2019
Edited: 03.10.2019
Version: Python 3.7.4

https://projecteuler.net/problem=27:
Euler discovered the remarkable quadratic formula: n²+n+41

It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39. However, when n=40, 40²+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41, 41²+41+41 is clearly divisible by 41.

The incredible formula n²−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n²+an+b, where |a|<1000 and |b|≤1000

where |n| is the modulus/absolute value of n
e.g. |11|=11 and |−4|=4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.
"""
import time
start_time = time.time()


def coefficient_product_from_quadratic_prime_expression(absolute_until):
    prime_cap = abs(absolute_until)
    primes = sieve_of_primes(until=prime_cap)
    maximum_number_of_primes, coefficients = 0, (None, None)

    for a in range(-abs(absolute_until) + 1, abs(absolute_until)):
        for b in range(3, abs(absolute_until), 2):
            n, candidate = 0, b
            while (candidate % 2 or candidate == 2) and candidate > 1 and primes[(candidate - 1) // 2 - 1]:
                n += 1
                candidate = n**2 + a * n + b

                while len(primes) < (candidate - 1) // 2:
                    prime_cap *= 2
                    primes = sieve_of_primes(until=prime_cap)

            if n > maximum_number_of_primes:
                maximum_number_of_primes = n
                coefficients = (a, b)

    return coefficients[0] * coefficients[-1]


def sieve_of_primes(until):
    sieve = [True] * ((until - 1) // 2)

    for i in range(len(sieve)):
        if sieve[i]:
            prime = 2 * (i + 1) + 1
            for r in range((prime**2 - 3) // 2, len(sieve), prime):
                sieve[r] = False
            if (prime**2 - 3) // 2 >= len(sieve):
                return sieve

    return sieve


def main():
    solution = coefficient_product_from_quadratic_prime_expression(absolute_until=10**3)

    print('Solution: %s.\nExecution time: %s seconds.' % (solution, time.time() - start_time))


if __name__ == '__main__':
    main()
