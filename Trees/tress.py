class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def inOrder(self):
        if self.left :
            self.left.inOrder()
        print(self.data,end=(" "))
        if self.right:
            self.right.inOrder()
          
    
    def postOrder(self):
        if self.left:
            self.left.postOrder()
        if self.right:
            self.right.postOrder()
        print(self.data,end=(" "))

    def preorder(self):
        print(self.data,end = (" "))
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

       

n = Node(30)
n.left = Node(20)
n.right = Node(10)
n.left.left = Node(10)
n.right.right= Node(5)

n.inOrder()
n.postOrder()
n.preorder()
