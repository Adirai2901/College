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
    return root 

def is_valid_bst(root, min_value=float('-inf'), max_value=float('inf')): 
    if root is None:
        return True
    if root.value <= min_value or root.value >= max_value:
        return False
    
    return (is_valid_bst(root.left, min_value, root.value) and is_valid_bst(root.right, root.value, max_value))

def display_tree(root, level=0):
    if root is not None:
        display_tree(root.right, level + 1)
        print( root.value)
        display_tree(root.left, level + 1)

root = None
keys = list(map(int, input("Enter keys to insert into the BST (space-separated): ").split()))
for key in keys:
    root = insert(root, key)

display_tree(root)


print(is_valid_bst(root))
