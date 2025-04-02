class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class ll:
    
    def __init__(self):
        self.head = None

    def print(self):

        if self.head is None:
            print("List is empty")
        
        temp = self.head
        while temp:
            print(temp.data,end=("->"))
            temp = temp.next
        print("None")

l = ll()
n = Node(10)
n1 = Node(20)
n2 = Node(30)
n3 = Node(40)
n4 = Node(50)
l.head = n
n.next = n1
n1.next = n2
n2.next = n3
n3.next=n4

l.print()
