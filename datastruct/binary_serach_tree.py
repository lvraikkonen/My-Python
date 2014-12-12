class Node:
    def __init__(self,val):
        self.l_child = None
        self.r_child = None
        self.data = val

## build BST
def binary_insert(root,node):
    if root is None:
        root = node
    else:
        if node.data < root.data:
            ## left
            if root.l_child is None:
                root.l_child = node
            else:
                binary_insert(root.l_child,node)
        else:
            ## right
            if root.r_child is None:
                root.r_child = node
            else:
                binary_insert(root.r_child,node)

def in_order_print(root):
    if not root:
        return
    in_order_print(root.l_child)
    print root.data
    in_order_print(root.r_child)
