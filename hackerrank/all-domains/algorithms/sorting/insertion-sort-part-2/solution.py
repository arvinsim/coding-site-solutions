# https://www.hackerrank.com/challenges/insertionsort2
# Python 3


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return arr


def insertionSort(items):
    for i in range(1, len(items)):
        for j in range(i-1, -1, -1):
            if items[j] > items[j+1]:
                items = swap(arr=items, i=j, j=j+1)
        print(' '.join(map(str, items)))

# m = input()
# ar = [int(i) for i in input().strip().split(' ')]
# insertionSort(ar)

list_of_numbers = [1, 4, 3, 5, 6, 2]
insertionSort(list_of_numbers)
"""
1 4 3 5 6 2
1 3 4 5 6 2
1 3 4 5 6 2
1 3 4 5 6 2
1 2 3 4 5 6
"""

# list_of_numbers = [9, 8, 6, 7, 3, 5, 4, 1, 2]
# insertionSort(list_of_numbers)
"""
9 8 6 7 3 5 4 1 2

8 9 6 7 3 5 4 1 2
6 8 9 7 3 5 4 1 2
6 7 8 9 3 5 4 1 2
3 6 7 8 9 5 4 1 2
3 5 6 7 8 9 4 1 2
3 4 5 6 7 8 9 1 2
1 3 4 5 6 7 8 9 2
1 2 3 4 5 6 7 8 9
"""