class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def min_Value(root):
    temp = root.left
    while root.left is not None:
        temp = temp.next
    print(temp.value)

def display_tree(root, level=0):
    if root is not None:
        display_tree(root.right, level + 1)
        print( root.val)
        display_tree(root.left, level + 1)

        
