# https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list
# Python 2

"""
 Insert Node at a specific position in a linked list
 head input could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

# This is a "method-only" submission.
# You only need to complete this method.
def InsertNth(head, data, position):
    if head is None:
        return Node(data=data)
    else:
        current = head

        if position == 0:
            node_to_insert = Node(data=data, next_node=current)
            return node_to_insert
        else:
            prev = None
            for i in xrange(position):
                prev = current
                current = current.next
            new_node = Node(data=data)
            prev.next = new_node
            new_node.next = current
            return head

# def display_linked_list(head):
#     s = ''
#     while True:
#         s += '{}->'.format(head.data)
#         if head.next == None:
#             break
#         else:
#             head = head.next
#     s += 'NULL'
#     print(s)
#
#
# # LL = Node(1)
# c = Node(3)
# b = Node(2, c)
# head = Node(1, b)
#
# head = InsertNth(head, 'x', 1)
#
# display_linked_list(head)

