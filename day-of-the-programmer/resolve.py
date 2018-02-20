#!/bin/python3

import sys


def solve(year):
    if year == 1918:
        feb = 15
    else:
        feb = 28
        if year <= 1917 and year % 4 == 0:
            feb = 29
        else:
            if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
                feb = 29
    day_of_programmer = 31 + feb + 31 + 30 + 31 + 30 + 31 + 31
    september_date = 256 - day_of_programmer
    return "%d.09.%d" % (september_date, year)


year = int(input().strip())
result = solve(year)
print(result)
