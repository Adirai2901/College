class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

n = Node(30)
n.left = Node(20)
n.right = Node(10)