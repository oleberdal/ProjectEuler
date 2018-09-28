"""
Author: Berdal, Ole
Created: 25.09.2018
Edited: 28.09.2018
Version: Python 3.7.0

https://projecteuler.net/problem=4:
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
import time
start_time = time.time()


def is_palindrome(n):
    n = str(n)
    return n == n[::-1]


def find_largest_palindrome(digits):
    palindromes = []
    for x in range(10**(digits - 1), 10**digits):
        for y in range(x, 10**digits):
            if is_palindrome(x * y):
                palindromes.append(x * y)

    return palindromes


def main():
    solution = max(find_largest_palindrome(3))

    print('Solution: %s.\nExecution time: %s seconds.' % (solution, time.time() - start_time))


if __name__ == '__main__':
    main()