"""
Author: Berdal, Ole
Created: 28.09.2018
Edited: 03.10.2019
Version: Python 3.7.4

https://projecteuler.net/problem=9:
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a² + b² = c²

For example, 3² + 4² = 9 + 16 = 25 = 5².

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import time
start_time = time.time()


def find_pythagorean_triplet(roof):
    for a in range(1, int(roof / (2 + 2**0.5)) + 1):
        b = roof * ((roof / 2) - a) / (roof - a)
        if b.is_integer() and a != b:
            return a, int(b), int(pythagorean(a, b))

    return [-1]


def pythagorean(x, y):
    return (x**2 + y**2)**0.5


def multiply_sequence(sequence):
    product = 1
    for number in sequence:
        product *= number

    return product


def main():
    solution = multiply_sequence(sequence=find_pythagorean_triplet(roof=10**3))

    print('Solution: %s.\nExecution time: %s seconds.' % (solution, time.time() - start_time))


if __name__ == '__main__':
    main()
