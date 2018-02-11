# https://www.hackerrank.com/challenges/ctci-linked-list-cycle
# Python 3

"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""

def has_cycle(node):
    c = node
    n = node.next

    while n is not None:
        if hasattr(c, 'visited'):
            return True
        c.visited = True
        c = n.next
        n = c.next
    return False


# TEST CODE
class Node(object):
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next = next_node


first_case = Node(1)

three = Node(3)
two = Node(2, three)
one = Node(1, two)
three.next = two

second_case = one

x = Node('x')
y = Node('y', x)
third_case = Node('third_case', y)

print('has_cycle(first_case): {}'.format(has_cycle(first_case)))
print('has_cycle(second_case): {}'.format(has_cycle(second_case)))
print('has_cycle(second_case): {}'.format(has_cycle(third_case)))
