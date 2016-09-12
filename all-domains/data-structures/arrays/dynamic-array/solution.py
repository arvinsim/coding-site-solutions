#!/usr/env/bin python
# https://www.hackerrank.com/challenges/dynamic-array
# Python 2


def get_initial_seq_list(N):
    seqList = []
    for i in xrange(N):
        seq = []
        # for j in xrange(N-1):
        #     seq.append(0)
        seqList.append(seq)
    return seqList


def query_1(seqList, x, y, lastAns, N):
    index = (x ^ lastAns) % N
    seqList[index].append(y)
    return seqList


def query_2(seqList, x, y, lastAns, N):
    index = (x ^ lastAns) % N
    seq = seqList[index]
    size = len(seq)
    newLastAns = seq[y % size]
    print(newLastAns)
    return newLastAns

# input = '2 5'
input = raw_input()
N, Q = map(lambda x: int(x), input.split(' '))
seqList = get_initial_seq_list(N)
lastAns = 0


# for input in ['1 0 5', '1 1 7', '1 0 3', '2 1 0', '2 1 1']:
for i in xrange(Q):
    input = raw_input()
    query, x, y = map(lambda x: int(x), input.split(' '))
    if query == 1:
        seqList = query_1(seqList, x, y, lastAns, N)
    elif query == 2:
        lastAns = query_2(seqList, x, y, lastAns, N)
    else:
        print('error')
