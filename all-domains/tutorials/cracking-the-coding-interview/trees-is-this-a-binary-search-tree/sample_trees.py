class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def get_simple_tree():
    """
        n1
          \
          n3
           \
           n4
          /  \
        n2   n5

    This is not a binary search tree
    """
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)

    n1.right = n3
    n3.right = n4
    n4.left = n2
    n4.right = n5

    return n1

def get_inorder_traversal_test_tree():
    """
            10
           /  \
          5   15
           \
           8
    It should output 5,8,10,15
    :return:
    """
    n5 = Node(5)
    n8 = Node(8)
    n10 = Node(10)
    n15 = Node(15)

    n10.left = n5
    n10.right = n15
    n5.right = n8
    return n10

def get_complex_tree():
    """
    This is not a binary search tree
    :return:
    """
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n8 = Node(8)
    n9 = Node(9)
    n10 = Node(10)
    n11 = Node(11)
    n12 = Node(12)
    n13 = Node(13)
    n14 = Node(14)
    n15 = Node(15)

    n8.left = n4
    n8.right = n13

    n4.left = n2
    n4.right = n6

    n2.left = n1
    n2.right = n3

    n6.left = n5
    n6.right = n7

    n13.left = n10
    n13.right = n14

    n10.left = n9
    n10.right = n11

    n14.left = n12
    n14.right = n15

    return n8

def get_binary_search_tree():
    """
            4
           /  \
          2    6
         / \  / \
        1  3 5  7

    This is a binary search tree
    :return:
    """
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)

    n4.left = n2
    n4.right = n6
    n2.left = n1
    n2.right = n3
    n6.left = n5
    n6.right = n7

    return n4

