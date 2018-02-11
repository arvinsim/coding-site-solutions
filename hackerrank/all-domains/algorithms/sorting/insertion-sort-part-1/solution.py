# https://www.hackerrank.com/challenges/insertionsort1
# Python 3


def formatted_print(items):
    formatted = ' '.join([str(item) for item in items])
    print(formatted)


def insertionSort(items):
    # The value to insert is the right most element
    length = len(items)-1
    value_to_insert = items[length]
    start = length-1  # we start at the second last item

    for index in range(start, -1, -1):
        item = items[index]
        items[index+1] = item

        if item < value_to_insert:
            items[index+1] = value_to_insert
            formatted_print(items)
            return

        formatted_print(items)

    # If all the elements are greater than the value to insert,
    # insert value at the start of the list
    items[0] = value_to_insert
    formatted_print(items)

n = input()
x = input()
# x = '2 4 6 8 3'
# x = '2 3 4 5 6 7 8 9 10 1'

items = [int(item) for item in x.split(' ')]
insertionSort(items)
