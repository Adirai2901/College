class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def tree(root,data):
    nd = Node(data)
    if root is None:
        return nd
    else:
        if data > root.data:
            root.right = tree(root.right,data)
        else:
            root.left = tree(root.left,data)
    return root


root = None

val = list(map(int,input("Enter the values").split()))

for val in val:
    root = tree(root,val)


def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data,end=(" "))
        inOrder(root.right)
inOrder(root)