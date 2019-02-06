"""
Author: Berdal, Ole
Created: 06.02.2019
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
    from_date, to_date, initial_date, initial_day, weekday = list(map(int, from_date.split('.'))), list(map(int, to_date.split('.'))), list(map(int, initial_date[0].split('.'))), weekdays.index(initial_date[1]), weekdays.index(weekday)
    checkedBelow = not date1_came_before_date2(from_date, initial_date)
    checkedAbove = date1_came_before_date2(to_date, initial_date)

    number_of_weekdays = 0

    date, day = initial_date.copy(), initial_day
    while not checkedBelow or not checkedAbove:
        days_relative = -1 if not checkedBelow else 1
        if date[0] == x and day % 7 == weekday and date1_came_before_date2(date, to_date) and not date1_came_before_date2(date, from_date):
            number_of_weekdays += 1
        if not checkedBelow and not date1_came_before_date2(from_date, date):
            checkedBelow = True
            date = initial_date.copy()
            day = initial_day
            days_relative = 1
        if not checkedAbove and date1_came_before_date2(to_date, date):
            checkedAbove = True
        date = days_relative_to_date(date, days_relative)
        day += days_relative

    return number_of_weekdays


def date1_came_before_date2(date1, date2):
    return date1[2] < date2[2] or (date1[2] == date2[2] and date1[1] < date2[1]) or (date1[2] == date2[2] and date1[1] == date2[1] and date1[0] < date2[0])


def days_relative_to_date(date, relative_day):
    days_in_month = days_in_months[date[1] - 1] if days_in_months[date[1] - 1] != 'check_leap_year' else is_leap_year(date[2])

    if not 1 <= date[0] + relative_day <= days_in_month:
        if relative_day == 1:
            date[0] -= days_in_month
            date[1] += 1
            if date[1] - 1 >= len(days_in_months):
                date[1] -= len(days_in_months)
                date[2] += 1
        else:
            if date[1] - 1 < 1:
                date[2] -= 1
                date[1] += len(days_in_months)
            date[0] += days_in_months[date[1] - 2] if days_in_months[date[1] - 2] != 'check_leap_year' else is_leap_year(date[2])
            date[1] -= 1
    date[0] += relative_day
    return date



def is_leap_year(year):
    if year % 4 or (not year % 100 and year % 400):
        return 28
    return 29


def main():
    global weekdays, days_in_months
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    days_in_months = [31, 'check_leap_year', 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    solution = number_of_weekdays_on_x_of_month(1, "Sunday", "1.1.101", "31.12.2000", ("17.05.1950", "Wednesday"))

    print('Solution: %s.\nExecution time: %s seconds.' % (solution, time.time() - start_time))


if __name__ == '__main__':
    main()
