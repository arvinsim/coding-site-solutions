#!/bin/python
#https://www.hackerrank.com/challenges/2d-array

# KEY INSIGHTS
# 1. Variables in list comprehensians are not encapsulated. They could shadow
# local variables if you name them the same
# 2. When looping 2-dimensional arrays, the outer loop should  represent the
# y-axis while the inner loop should represent the x-axis

import sys

ARRAY_DIMENSION = 6
HOURGLASS_WIDTH = 3
HOURGLASS_HEIGHT = 3


def get_2d_array_visualization(items):
    visualization = ''
    for rows in items:
        visualization += ' '.join([str(row) for row in rows]) + '\n'
    return visualization


def get_array_input():
    # return [
    #     [1, 1, 1, 0, 0, 0],
    #     [0, 1, 0, 0, 0, 0],
    #     [1, 1, 1, 0, 0, 0],
    #     [0, 9, 2, -4, -4, 0],
    #     [0, 0, 0, -2, 0, 0],
    #     [0, 0, -1, -2, -4, 0],
    # ]
    # return [
    #     [-1, -1, 0, -9, -2, -2, ],
    #     [-2, -1, -6, -8, -2, -5],
    #     [-1, -1, -1, -2, -3, -4],
    #     [-1, -9, -2, -4, -4, -5],
    #     [-7, -3, -3, -2, -9, -9],
    #     [-1, -3, -1, -2, -4, -5],
    # ]
    arr = []
    for arr_i in xrange(ARRAY_DIMENSION):
        arr_temp = map(int,raw_input().strip().split(' '))
        arr.append(arr_temp)
    return arr


def is_part_of_hourglass(x, y):
    if (x == 1 and y == 0) or (x == 1 and y == 2):
        return False
    else:
        return True


def get_hourglass_sum(hourglass):
    s = 0
    for row in hourglass:
        for item in row:
            s += item
    return s


def get_hourglass(arr, x, y):
    hourglass = [[0 for foo in xrange(HOURGLASS_WIDTH)] for bar in xrange(HOURGLASS_HEIGHT)]
    for b in xrange(HOURGLASS_HEIGHT):
        for a in xrange(HOURGLASS_WIDTH):
            if is_part_of_hourglass(a, b):
                current_x = a + x
                current_y = b + y
                hourglass[a][b] = arr[current_x][current_y]
    return hourglass

arr = get_array_input()
greatest_sum = None
for x in xrange(ARRAY_DIMENSION - HOURGLASS_WIDTH + 1):
    for y in xrange(ARRAY_DIMENSION - HOURGLASS_HEIGHT + 1):
        hg = get_hourglass(arr, x, y)
        shg = get_hourglass_sum(hg)

        # print(get_2d_array_visualization(hg))
        # print(shg)
        # print('==========')

        if greatest_sum is None:
            greatest_sum = shg

        if shg > greatest_sum:
            greatest_sum = shg
            
print(greatest_sum)

