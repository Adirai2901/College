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
        if data < root.data:
            root.left = tree(root.left,data)
        else:
            root.right = tree(root.right,data)
    return root


root = None

values = list(map(int,input("Enter the values: ").split()))

for values in (values):
    root = tree(root,values)

def inorder(root):
    if root :
        inorder(root.left)
        print(root.data,end=(" "))
        inorder(root.right)
inorder(root)