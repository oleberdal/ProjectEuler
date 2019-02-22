"""
Author: Berdal, Ole
Created: 06.02.2019
Edited: 07.02.2019
Version: Python 3.6.7

https://projecteuler.net/problem=19:
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""
import time
start_time = time.time()


def number_of_weekdays_on_x_of_month(x, weekday, from_date, to_date, initial_date):
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    from_date, to_date = tuple(map(int, from_date.split('.'))), tuple(map(int, to_date.split('.')))
    initial_date, initial_day = list(map(int, initial_date[0].split('.'))), weekdays.index(initial_date[1])
    weekday = weekdays.index(weekday)

    checked_below = not date1_before_date2(date1=from_date, date2=initial_date)
    checked_above = date1_before_date2(date1=to_date, date2=initial_date)

    number_of_weekdays = 0

    date = initial_date.copy() if not checked_below else next_date(date=initial_date, step=-1)
    day = initial_day - (0 if not checked_below else 1)
    step = -1 if not checked_below else 1
    while not checked_below or not checked_above:
        date = next_date(date=date, step=step)
        day += step
        if date[0] == x and day % 7 == weekday and not date1_before_date2(date1=to_date, date2=date) and not date1_before_date2(date1=date, date2=from_date):
            number_of_weekdays += 1
        if not checked_below and not date1_before_date2(date1=from_date, date2=date):
            checked_below = True
            date = next_date(date=initial_date, step=step)
            day = initial_day
            step = 1
        elif not checked_above and not date1_before_date2(date1=date, date2=to_date):
            checked_above = True

    return number_of_weekdays


def date1_before_date2(date1, date2):
    return date1[2] < date2[2] or date1[2] == date2[2] and date1[1] < date2[1] or date1[2] == date2[2] and date1[1] == date2[1] and date1[0] < date2[0]


def next_date(date, step):
    if not 1 <= date[0] + step <= days_in_month(month=date[1], year=date[2]):
        if not 1 <= date[1] + step <= 12:
            date[2] += step
            date[1] -= step * 12
        date[1] += step
        date[0] -= step * days_in_month(month=date[1] - bool(step == 1), year=date[2])
    date[0] += step

    return date


def days_in_month(month, year):
    days_in_months = [31, 28 + bool(not year % 4 and year % 100 or not year % 400), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    return days_in_months[month - 1]


def main():
    solution = number_of_weekdays_on_x_of_month(x=1, weekday="Sunday", from_date="01.01.1901", to_date="31.12.2000", initial_date=("01.01.1900", "Monday"))

    print('Solution: %s.\nExecution time: %s seconds.' % (solution, time.time() - start_time))


if __name__ == '__main__':
    main()
