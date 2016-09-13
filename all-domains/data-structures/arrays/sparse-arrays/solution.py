#!/usr/env/bin python
# https://www.hackerrank.com/challenges/sparse-arrays
# Python 2

# N = '4'
# items = ['aba', 'baba', 'aba', 'xzxb']
# Q = '3'
# queries = ['aba', 'xzxb', 'ab']
N = int(raw_input())
items = []
for i in xrange(N):
    items.append(raw_input())

Q = int(raw_input())
queries = []
for j in xrange(Q):
    queries.append(raw_input())

for query in queries:
    print(items.count(query))

