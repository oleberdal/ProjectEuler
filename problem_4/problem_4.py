"""
Author: Berdal, Ole
Created: 25.09.2018
Version: Python 3.7.0

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
import time
start_time = time.time()

def is_palindrome(n):
    n = str(n)
    return n == n[::-1]

def find_largest_palindrome():
    palindromes = []
    for x in range(100, 1000):
        for y in range(x, 1000):
            product = x*y
            if is_palindrome(product):
                palindromes.append(product)
    return palindromes

solution = max(find_largest_palindrome())

print("Solution: %s.\nExecution time: %s seconds." % (solution, time.time() - start_time))