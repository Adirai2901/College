class Branches:
    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Branches(key)
    else:
        if root.value < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)

def is_vaild_bst(root, min_value=float('-inf'), max_value=float('inf')):
    if root is None:
        return True
    if root.value <= min_value or root.value >= max_value:
        return False
    
    return (is_valid_bst(root.left, min_value, root.value) and is_valid_bst(root.right, root.value, max_value))

def display_tree(root, level=0):
    if root is not None:
        display_tree(root.right, level + 1)
        print(' ' * 4 * level + '->', root.value)
        display_tree(root.left, level + 1)

def find_min(root):
    temp  = root
    while temp.left is not None:
        temp = temp.left
    return temp.value

def find_max(root):
    temp = root
    while temp.right is not None:
        temp = temp.right
    return temp.value

root = None
print("Insert keys into the BST")
keys = [10, 5, 15, 3, 7, 12, 18]
for key in keys:
    root = insert(root, key)
