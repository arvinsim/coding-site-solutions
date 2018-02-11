#!/usr/env/bin python
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list
# Python 2

# first_line = '4'
# second_line = '57 57 -57 57'

first_line = raw_input()
second_line = raw_input()

n = int(first_line)
numbers = [int(x) for x in second_line.split(' ')]

unique_numbers = []
for number in numbers: 
    if number not in unique_numbers:
        unique_numbers.append(number)

unique_numbers.sort()
unique_numbers.reverse()
print(unique_numbers[1])