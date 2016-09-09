#!/usr/env/bin python
# https://www.hackerrank.com/challenges/py-if-else
# Python 2

n = int(raw_input())
WEIRD = 'Weird'
NOT_WEIRD = 'Not Weird'

if n % 2 == 1:
    print(WEIRD)
else:
    if n >= 2 and n <= 5:
        print(NOT_WEIRD)
    elif n >= 6 and n <= 20:
        print(WEIRD)
    elif n > 20:
        print(NOT_WEIRD)
