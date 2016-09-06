# Day 0: Mean, Median, and Mode
# https://www.hackerrank.com/challenges/s10-basic-statistics

from __future__ import division

# TODO: Fix inputs
def get_input_elements():
    number_of_items = input()
    elements = []
    for index in range(number_of_items):
        elements.append(input())
    return elements


def get_mean(elements):
    """The average of all the integers in a set of values."""
    s = 0
    for element in elements:
        s += element
    return (s / len(elements))


def get_median(elements):
    """The midpoint value of a data set for which an equal number of samples are
    less than and greater than the value. For an odd sample size, this is the
    middle element of the sorted sample; for an even sample size, this is the
    average of the  middle elements of the sorted sample."""
    elements.sort()
    length_of_elements = len(elements)
    mid_position = length_of_elements // 2
    if length_of_elements % 2 == 0:
        # for even number of items, the median is the average of the 2 middle
        # elements
        sum_of_the_mids = (elements[mid_position - 1] + elements[mid_position])
        median = sum_of_the_mids / 2
    else:
        # for odd number of items, the median is the middle element
        median = elements[mid_position]
    return median


def get_mode(elements):
    """The element(s) that occur most frequently in a data set."""
    dictionary = {}
    elements.sort()
    for element in elements:
        if element in dictionary:
            dictionary[element] += 1
        else:
            dictionary[element] = 1

    mode = elements[0]
    highest_count = 0
    for key, value in dictionary.items():
        if highest_count <= value and mode > key:
            mode = key
            highest_count = value
    return mode

elements = get_input_elements()
mean = get_mean(elements)
median = get_median(elements)
mode = get_mode(elements)

print(mean)
print(median)
print(mode)
