"""
Author: Berdal, Ole
Created: 18.10.2019
Version: Python 3.7.4

https://projecteuler.net/problem=31:
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:
1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?
"""
import time
start_time = time.time()

memoization = dict()


def possible_coin_combinations_to_make_amount(coins, amount):
    global memoization
    if len(coins) == 1:
        memoization[coins, amount] = not amount % coins[0]
        return not amount % coins[0]

    combination_counter, number_of_occurrences, current_coin, remaining_coins = 0, 0, coins[0], coins[1:]
    while number_of_occurrences * current_coin <= amount:
        remaining_amount = amount - (number_of_occurrences * current_coin)
        if (remaining_coins, remaining_amount) in memoization:
            combination_counter += memoization[remaining_coins, remaining_amount]
        else:
            combination_counter += possible_coin_combinations_to_make_amount(coins=remaining_coins, amount=remaining_amount)
        number_of_occurrences += 1

    memoization[coins, amount] = combination_counter
    return combination_counter


def main():
    with open('data/coins', 'r') as file:
        lines = file.readlines()

    coins = tuple(sorted(map(int, lines), reverse=True))

    solution = possible_coin_combinations_to_make_amount(coins=coins, amount=1000)

    print('Solution: %s.\nExecution time: %s seconds.' % (solution, time.time() - start_time))


if __name__ == '__main__':
    main()
