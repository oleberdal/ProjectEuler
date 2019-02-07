"""
Author: Berdal, Ole
Created: 05.02.2019
Edited: 07.02.2019
Version: Python 3.6.7

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
    collatz_chain_length = {1:1}

    for x in range(maximum - 1, 1, -1):
        collatz(x, collatz_chain_length)

    return list(collatz_chain_length)[list(collatz_chain_length.values()).index(max(collatz_chain_length.values()))]


def collatz(number, collatz_chain):
    if number not in collatz_chain:
        next_collatz = number // 2 if not number % 2 else 3 * number + 1
        collatz(next_collatz, collatz_chain)
        collatz_chain[number] = collatz_chain[next_collatz] + 1


def main():
    solution = longest_collatz_chain_below(1000000)

    print('Solution: %s.\nExecution time: %s seconds.' % (solution, time.time() - start_time))


if __name__ == '__main__':
    main()
