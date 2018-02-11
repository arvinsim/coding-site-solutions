# https://www.hackerrank.com/challenges/ctci-lonely-integer
#!/bin/python3

import sys

def lonely_integer(a):
    value = 0
    for x in a:
        prev_value = value
        new_value = value ^ x
        value = new_value
    return value


# n = int(input().strip())
# a = [int(a_temp) for a_temp in input().strip().split(' ')]
n = 5
a = [0, 0, 1, 2, 1]
print(lonely_integer(a))


test = 3 + 12
print(test ^ 3)
print(test ^ 12)

