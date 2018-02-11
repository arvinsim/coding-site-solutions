#!/usr/env/bin python
# https://www.hackerrank.com/challenges/write-a-function
# Python 2


def is_divisible_by(number, year):
    return year % number == 0


def is_leap(year):
    leap = False
    if is_divisible_by(4, year):
        leap = True
        if is_divisible_by(100, year):
            leap = False
            if is_divisible_by(400, year):
                leap = True
    return leap
