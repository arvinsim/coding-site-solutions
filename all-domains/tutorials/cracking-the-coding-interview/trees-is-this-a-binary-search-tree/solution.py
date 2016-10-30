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
from solution_min_max import is_binary_search_tree as isbst1
from solution_traversal_with_list import is_binary_search_tree as isbst2

# def inorder_traversal(root):
#     if root.left is not None:
#         inorder_traversal(root.left)
#     print(root.data)
#     if root.right is not None:
#         inorder_traversal(root.right)


def check_binary_search_tree_(root):
    # Solution #1
    # INT_MIN = -9999999999999
    # INT_MAX = 9999999999999
    # return isbst1(root, INT_MIN, INT_MAX)

    # Solution #2
    # return isbst2(root)

print(check_binary_search_tree_(get_simple_tree())) # Should return False
print(check_binary_search_tree_(get_complex_tree())) # Should return False
print(check_binary_search_tree_(get_binary_search_tree())) # Should return True
