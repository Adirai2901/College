class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def tree(root,data):
    if root is None:
        return Node(data)
    else:
        if data < root.data:
            root.left = tree(root.left,data)
        else:
            root.right = tree(root.right,data)
    return root

def levelOrder(root):
    if root is None:
        return
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.data, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

elements = [20, 10, 30, 5, 15, 25, 35]
root = None
for element in elements:
    root = tree(root, element)
                
print("Level Order Traversal of the tree:")
levelOrder(root)