"""
Author: Berdal, Ole
Created: 28.09.2018
Edited: 01.10.2018
Version: Python 3.7.0

https://projecteuler.net/problem=9:
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import time
start_time = time.time()


def find_pythagorean_triplet(roof):
    for a in range(1, int(roof / (2 + 2**0.5)) + 1):
        b = (roof * (a - (roof / 2))) / (a - roof)
        if b.is_integer() and a != b:
            return [a, int(b), int(pythagorean(a, b))]

    return [-1]


def pythagorean(x, y):
    return (x**2 + y**2)**0.5


def multiply_sequence(sequence):
    product = 1
    for x in range(len(sequence)):
        product *= sequence[x]

    return product


def main():
    solution = multiply_sequence(find_pythagorean_triplet(1000))

    print('Solution: %s.\nExecution time: %s seconds.' % (solution, time.time() - start_time))


if __name__ == '__main__':
    main()
