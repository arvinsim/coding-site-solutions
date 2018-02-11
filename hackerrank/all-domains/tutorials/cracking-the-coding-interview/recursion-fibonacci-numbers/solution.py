# https://www.hackerrank.com/challenges/ctci-fibonacci-numbers
# Python 3

# I need to memoize, otherwise the Hackerrank tests would time out
fibcache = {}
def fibonacci(n):
    """
    :param n:
    :return:
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n not in fibcache:
        fibcache[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return fibcache[n]

n = int(input())
# n = 10
print(fibonacci(n))
