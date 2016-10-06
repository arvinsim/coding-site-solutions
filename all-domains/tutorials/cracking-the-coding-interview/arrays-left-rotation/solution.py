# https://www.hackerrank.com/challenges/ctci-array-left-rotation
#  Python 3

def array_left_rotation(a, n, k):
    # Convert generator to a list
    arr = list(a)
    for _ in range(k):
        temp = arr.pop(0)
        arr.append(temp)
    # Return a generator from the list
    return (x for x in arr)

n, k = map(int, input().strip().split(' '))
a = map(int, input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')

