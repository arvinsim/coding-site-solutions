# https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks
# Python 3


class MyQueue(object):
    def __init__(self):
        self.enqueue = []
        self.dequeue = []

    def peek(self):
        if len(self.dequeue) > 0:
            return self.dequeue[0]

    def pop(self):
        while len(self.enqueue) > 0:
            self.dequeue.append(self.enqueue.pop())
        if len(self.dequeue) > 0:
            return self.dequeue.pop()

    def put(self, value):
        self.enqueue.append(value)

queue = MyQueue()
t = [
   '1 42',
   '2',
   '1 14',
   '3',
   '1 28',
   '3',
   '1 60',
   '1 78',
   '2',
   '2',
]
for line in t:
    values = map(int, line.split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())

# queue = MyQueue()
# t = int(input())
# for line in range(t):
#     values = map(int, input().split())
#     values = list(values)
#     if values[0] == 1:
#         queue.put(values[1])
#     elif values[0] == 2:
#         queue.pop()
#     else:
#         print(queue.peek())

