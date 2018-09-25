"""
Author: Berdal, Ole
Created: 25.09.2018
Version: Python 3.7.0

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
import time
start_time = time.time()

solution = 0

for x in range(1000):
    if not x % 3 or not x % 5:
        solution += x

print("Solution: %s.\nExecution time: %s seconds." % (solution, time.time() - start_time))