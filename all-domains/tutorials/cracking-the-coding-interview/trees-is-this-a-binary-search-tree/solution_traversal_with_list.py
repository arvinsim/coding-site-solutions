########################################################
# Solution #2 Inorder Traversal , store values in tree
#######################################################$
global value_list


def put_values_to_list_using_inorder_traversal(root):
    global value_list
    if root.left is not None:
        put_values_to_list_using_inorder_traversal(root.left)
    value_list.append(root.data)
    if root.right is not None:
        put_values_to_list_using_inorder_traversal(root.right)


def is_binary_search_tree(root):
    global value_list
    value_list = []
    print(value_list)
    put_values_to_list_using_inorder_traversal(root)
    print(value_list)
    len_for_range = len(value_list) - 1
    for i in range(len_for_range):
        if value_list[i] >= value_list[i+1]:
            return False
    return True



