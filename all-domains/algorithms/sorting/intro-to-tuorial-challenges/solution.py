# https://www.hackerrank.com/challenges/tutorial-intro
# Python 3

# number = 4
# n = 6
# x = '1 4 5 7 9 12'
# list_of_numbers = [item for item in map(lambda x: int(x), x.split(' '))]

number = int(input())
n = int(input())
list_of_numbers = [item for item in map(lambda x: int(x), input().split(' '))]

print(list_of_numbers.index(number))


