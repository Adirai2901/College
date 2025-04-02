class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class ll:
    def __init__(self):
        self.head = None

    def display(self):
        
        if self.head is None:
            print("None")
            
        temp = self.head
        while temp:
            print(temp.data,end=("->"))
            temp = temp.next
        print("None")

       

       
l = ll()

n = Node(10)
n1 = Node(20)
n.next =n1
l.head = n

l.display()

