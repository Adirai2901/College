class Tree:
    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Tree(key)
    else:
        if root.value < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

    