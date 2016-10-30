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

import sys
from sample_trees import get_simple_tree, get_complex_tree, get_binary_search_tree

simple_tree = get_simple_tree()
complex_tree = get_complex_tree()


def inorder_traversal(root):
    if root.left is not None:
        inorder_traversal(root.left)
    print(root.data)
    if root.right is not None:
        inorder_traversal(root.right)

# Arbitrary since Python 3 does not have a limit
INT_MIN = -9999999999999
INT_MAX = 9999999999999

def check_binary_search_tree_efficient(node, minimum, maximum):
    if node is None:
        return True

    if node.data < minimum or node.data > maximum:
        return False

    return check_binary_search_tree_efficient(node.left, minimum, node.data-1) and check_binary_search_tree_efficient(node.right, node.data+1, maximum)

def check_binary_search_tree_(root):
    return check_binary_search_tree_efficient(root, INT_MIN, INT_MAX)

# print(check_binary_search_tree_(simple_tree)) # Should return False
# print(check_binary_search_tree_(complex_tree)) # Should return False
# print(check_binary_search_tree_(get_binary_search_tree())) # Should return False
