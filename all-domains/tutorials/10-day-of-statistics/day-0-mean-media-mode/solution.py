# Day 0: Mean, Median, and Mode
# https://www.hackerrank.com/challenges/s10-basic-statistics
# Python 2


from __future__ import division

def get_input_elements():
    number_of_items = raw_input()
    if number_of_items < 10 and number_of_items > 2500:
        sys.exit('The number of items is < 10 or > 2500')
    list_of_numbers = raw_input()
    elements = list_of_numbers.split(' ')
    return [int(element) for element in elements]

# def get_input_elements():
#     number_of_items = ""
#     with open('input04.txt') as f:
#         number_of_items = f.readline()
#         if number_of_items < 10 and number_of_items > 2500:
#             sys.exit('The number of items is < 10 or > 2500')
#         list_of_numbers = f.readline()
#         elements = list_of_numbers.split(' ')
#         return [int(element) for element in elements]

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

    # Get the max value
    max_value = max(dictionary.values())
    highest_elements = [key for key, value in dictionary.items() if value == max_value]
    modes = sorted(highest_elements)
    return modes[0]

elements = get_input_elements()
mean = get_mean(elements)
median = get_median(elements)
mode = get_mode(elements)

print(round(mean, 1))
print(round(median, 1))
print(mode)
