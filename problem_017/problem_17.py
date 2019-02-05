"""
Author: Berdal, Ole
Created: 05.02.2019
Version: Python 3.6.7

https://projecteuler.net/problem=17:
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""
import time
start_time = time.time()


def number_of_letters_between(start, end):
    number_of_letters = 0

    for n in range(start, end + 1):
        number_of_letters += len(numerical_to_textual(n, textual_numbers.copy()).replace(' ', '').replace('-', ''))

    return number_of_letters


def numerical_to_textual(n, dictionary):
    if n == 0:
        return ''
    maximum_magnitude = max(dictionary)
    del dictionary[max(dictionary)]
    if n // maximum_magnitude < 1:
        return numerical_to_textual(n, dictionary)
    word = (numerical_to_textual(n // maximum_magnitude, dictionary.copy()) if maximum_magnitude >= 100 else '') + textual_numbers[maximum_magnitude]
    word += ' and ' if maximum_magnitude >= 100 and 0 < n % maximum_magnitude < 100 else ('-' if 0 < n % maximum_magnitude < 20 else ' ')
    word += numerical_to_textual(n % maximum_magnitude, dictionary)
    return word


def main():
    global textual_numbers
    textual_numbers = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight',
                       9:'nine', 10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen',
                       16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty', 30:'thirty', 40:'forty',
                       50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety', 100:'hundred', 1000:'thousand',
                       1000000:'million', 1000000000:'billion', 1000000000000:'trillion'}

    solution = number_of_letters_from_one_to(1, 1000)

    print('Solution: %s.\nExecution time: %s seconds.' % (solution, time.time() - start_time))


if __name__ == '__main__':
    main()
