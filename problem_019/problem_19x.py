"""
Author: Berdal, Ole
Created: 07.02.2019
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


def first_of_month(day, year_start, year_end):
    total = 0
    for year in range(year_start, year_end + 1):
        for month in range(1, 13):
            if day_of_week(year, month, 1) == day:
                total += 1
    return total


def day_of_week(year, month, day):
    d = day
    m = (month - 3) % 12 + 1
    y = year - 1 if m > 10 else year
    y, c = y % 100, (y - (y % 100)) / 100

    w = (d + floor(2.6 * m - 0.2) + y + floor(y / 4) + floor(c / 4) - 2 * c - 1) % 7

    return int(w)


def floor(n):
    return int(n) if n >= 0 or int(n) == n else int(n) - 1


def main():
    solution = first_of_month(6, 1901, 2000)

    print('Solution: %s.\nExecution time: %s seconds.' % (solution, time.time() - start_time))


if __name__ == '__main__':
    main()
