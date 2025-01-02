# You are given the following information, but you may prefer to do some research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

import time
import math

start_time = time.time()

days_not = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def daysForYear(year):
    if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
        return days_leap
    else:
        return days_not

year = 1900
days = 1
sundays = 0

# We know 1 Jan 1900 is Monday, what is 1 Jan 1901,
# which is where we want to start counting?
months = daysForYear(year)
for month in months:
    days += month
year += 1

while (year != 2001):
    months = daysForYear(year)
    for month in months:
        days %= 7
        if (days == 0):
            sundays += 1
        days += month
    year += 1

print(f"num sundays {sundays}")

print(f"--- Number of seconds to solve {time.time() - start_time}")


