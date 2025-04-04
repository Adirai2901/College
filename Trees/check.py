class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

n = Node(30)
n.left = Node(20)
n.right = Node(10)

def inorder(root):
    if root :
        inorder(root.left)
        print(root.data,end=(" "))
        inorder(root.right)
inorder(n)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data,end=(" "))
postorder(n)    

def preorder(root):
    if root:
        print(root.data,end=(" "))
        preorder(root.left)
        preorder(root.right)    
preorder(n)