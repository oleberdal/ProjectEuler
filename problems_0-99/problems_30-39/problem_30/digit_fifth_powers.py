"""
Author: Berdal, Ole
Created: 04.10.2019
Version: Python 3.7.4

https://projecteuler.net/problem=30:
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1⁴ + 6⁴ + 3⁴ + 4⁴
8208 = 8⁴ + 2⁴ + 0⁴ + 8⁴
9474 = 9⁴ + 4⁴ + 7⁴ + 4⁴
As 1 = 1⁴ is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""
import time
start_time = time.time()


def sum_of_numbers_whose_sum_of_nth_power_of_digits_is_same(power):
    total = 0

    number_of_digits = 1
    while number_of_digits * 9**power >= 10**number_of_digits:
        number_of_digits += 1

    digits = [0] * number_of_digits
    while sum(digits) < 9 * number_of_digits:
        for d in range(-1, -number_of_digits, -1):
            if digits[d] < digits[d - 1]:
                digits[d] += 1
                break
            else:
                digits[d] = 0
        else:
            digits[0] += 1

        temp_digits = digits.copy()
        for d in str(sum([d**power for d in digits])):
            if int(d) not in temp_digits:
                break
            temp_digits.remove(int(d))
        else:
            if len(temp_digits) < number_of_digits - 2 and (set(temp_digits) == {0} or temp_digits == []):
                total += sum([digit**power for digit in digits])

    return total


def main():
    solution = sum_of_numbers_whose_sum_of_nth_power_of_digits_is_same(power=5)

    print('Solution: %s.\nExecution time: %s seconds.' % (solution, time.time() - start_time))


if __name__ == '__main__':
    main()
