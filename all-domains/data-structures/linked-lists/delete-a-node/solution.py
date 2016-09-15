# https://www.hackerrank.com/challenges/delete-a-node-from-a-linked-list
# Python 2

"""
 Delete Node at a given position in a linked list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def Delete(head, position):
    if head.next is None:
        return None

    prev = None
    current = head

    for i in xrange(position):
        prev = current
        current = current.next

    if current == head:
        head = current.next
        current.next = None
    else:
        prev.next = current.next
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
# display_linked_list(head)
# head = Delete(head, 1)
# display_linked_list(head)
