"""
Author: Berdal, Ole
Created: 22.02.2019
Version: Python 3.6.7

https://projecteuler.net/problem=25:
The Fibonacci sequence is defined by the recurrence relation:

F_n = F_(n−1) + F_(n−2), where F_1 = 1 and F_2 = 1.
Hence the first 12 terms will be:

F_1 = 1
F_2 = 1
F_3 = 2
F_4 = 3
F_5 = 5
F_6 = 8
F_7 = 13
F_8 = 21
F_9 = 34
F_10 = 55
F_11 = 89
F_12 = 144
The 12th term, F_12, is the first term to contain three digits.

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
