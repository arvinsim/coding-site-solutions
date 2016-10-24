# https://www.hackerrank.com/challenges/ctci-is-binary-search-tree
# Python 3

""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

"""
For the purposes of this challenge, we define a binary search tree to be a binary tree with the following ordering properties:

- The value of every node in a node's left subtree is less than the data value of that node.
- The value of every node in a node's right subtree is greater than the data value of that node.

Note: A binary tree is not a binary search if there are duplicate values.
"""

from sample_trees import get_simple_tree, get_complex_tree

simple_tree = get_simple_tree()
complex_tree = get_complex_tree()

def check_binary_search_tree_(root):
    if root is None:
        return True

    left = root.left
    right = root.right
    data = root.data

    if left is not None:
        if left.data >= data:
            return False
    if right is not None:
        if right.data <= data:
            return False

print(check_binary_search_tree_(simple_tree)) # Should return False
# print(check_binary_search_tree_(complex_tree)) # Should return False
