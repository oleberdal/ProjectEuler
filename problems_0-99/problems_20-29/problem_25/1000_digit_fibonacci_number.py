"""
Author: Berdal, Ole
Created: 22.02.2019
Version: Python 3.6.7

https://projecteuler.net/problem=25:
The Fibonacci sequence is defined by the recurrence relation:

Fₙ = Fₙ₋₁ + Fₙ₋₂, where F₁ = 1 and F₂ = 1.
Hence the first 12 terms will be:

F₁ = 1
F₂ = 1
F₃ = 2
F₄ = 3
F₅ = 5
F₆ = 8
F₇ = 13
F₈ = 21
F₉ = 34
F₁₀ = 55
F₁₁ = 89
F₁₂ = 144
The 12th term, F₁₂, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""
import time
start_time = time.time()


def index_of_first_term_with_x_digits(digits):
    fib_a, fib_b, i = 1, 1, 2

    while fib_b // 10**(digits - 1) < 1:
        fib_a, fib_b, i = fib_b, fib_a + fib_b, i + 1

    return i


def main():
    solution = index_of_first_term_with_x_digits(digits=1000)

    print('Solution: %s.\nExecution time: %s seconds.' % (solution, time.time() - start_time))


if __name__ == '__main__':
    main()
