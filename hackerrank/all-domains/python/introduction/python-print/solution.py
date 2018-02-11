#!/usr/env/bin python
# https://www.hackerrank.com/challenges/python-print
# Python 2

N = int(raw_input())
# N = 3

print(reduce(lambda x, y: x + y, [str(n+1) for n in xrange(N)]))
