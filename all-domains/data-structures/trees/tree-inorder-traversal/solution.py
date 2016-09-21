# https://www.hackerrank.com/challenges/tree-inorder-traversal
# Python 2

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""

def inOrder(tree):
    if tree is None: return
    inOrder(tree.left)
    print(tree.data),
    inOrder(tree.right)

class Node:
    def __init__(self, left=None, right=None, data=None):
        self.left = left
        self.right = right
        self.data = data


one = Node(data=1)
four = Node(data=4)
six = Node(data=6)

five = Node(left=one, right=four, data=5)
two = Node(left=six, data=2)
three = Node(left=five, right=two, data=3)

inOrder(three)
