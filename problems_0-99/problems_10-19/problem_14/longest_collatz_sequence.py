"""
Author: Berdal, Ole
Created: 05.02.2019
Edited: 03.10.2019
Version: Python 3.7.4

https://projecteuler.net/problem=14:
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
import time
start_time = time.time()


def longest_collatz_chain_below(maximum):
    global collatz_chain_lengths
    collatz_chain_lengths = {1: 1}

    for n in range(maximum - 1, 1, -1):
        collatz(number=n)

    return max(collatz_chain_lengths, key=collatz_chain_lengths.get)


def collatz(number):
    if number not in collatz_chain_lengths:
        next_collatz = number // 2 if not number % 2 else 3 * number + 1
        collatz(number=next_collatz)
        collatz_chain_lengths[number] = collatz_chain_lengths[next_collatz] + 1


def main():
    solution = longest_collatz_chain_below(maximum=10**6)

    print('Solution: %s.\nExecution time: %s seconds.' % (solution, time.time() - start_time))


if __name__ == '__main__':
    main()
