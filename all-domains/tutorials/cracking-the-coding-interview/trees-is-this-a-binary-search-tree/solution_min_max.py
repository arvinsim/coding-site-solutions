##################################################
# Solution #1
##################################################

def is_binary_search_tree(node, minimum, maximum):
    if node is None:
        return True

    if node.data < minimum or node.data > maximum:
        return False

    return is_binary_search_tree(node.left, minimum, node.data-1) and \
           is_binary_search_tree(node.right, node.data+1, maximum)
