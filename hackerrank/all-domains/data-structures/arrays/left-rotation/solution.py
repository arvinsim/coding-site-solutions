#!/usr/env/bin python
# https://www.hackerrank.com/challenges/array-left-rotation
# Python 2

# first_input = '5 4'
# second_input = '1 2 3 4 5'
first_input = raw_input()
second_input = raw_input()

n, d = map(lambda x: int(x), first_input.split(' '))
items = second_input.split(' ')

for i in xrange(d):
    item = items.pop(0)
    items.append(item)

print(" ".join(items))
