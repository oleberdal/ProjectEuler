"""
Author: Berdal, Ole
Created: 05.02.2019
Edited: 03.10.2019
Version: Python 3.7.4

https://projecteuler.net/problem=17:
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""
import time
start_time = time.time()


def number_of_letters_between(start, end, vocabulary):
    number_of_letters = 0

    for n in range(start, end + 1):
        number_of_letters += len(numerical_to_textual(n=n, dictionary=vocabulary.copy()).replace(' ', '').replace('-', ''))

    return number_of_letters


def numerical_to_textual(n, dictionary):
    if n == 0:
        return ''

    maximum_magnitude = max(dictionary)
    textual = dictionary[maximum_magnitude]

    if n // maximum_magnitude == 0:
        del dictionary[max(dictionary)]
        return numerical_to_textual(n=n, dictionary=dictionary)

    word = (numerical_to_textual(n=n // maximum_magnitude, dictionary=dictionary.copy()) if maximum_magnitude >= 100 else '') + textual + (' and ' if 0 < n % maximum_magnitude < 100 <= maximum_magnitude else ('-' if 0 < n % maximum_magnitude < 20 else ' '))
    del dictionary[max(dictionary)]
    word += numerical_to_textual(n=n % maximum_magnitude, dictionary=dictionary)

    return word


def main():
    with open('data/vocabulary', 'r') as file:
        line = file.readline()

    vocabulary = {int(element.split(':')[0]): element.split(':')[1] for element in line.split(',')}

    solution = number_of_letters_between(start=1, end=10**3, vocabulary=vocabulary)

    print('Solution: %s.\nExecution time: %s seconds.' % (solution, time.time() - start_time))


if __name__ == '__main__':
    main()
