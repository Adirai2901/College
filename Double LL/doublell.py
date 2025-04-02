class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class DLL:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("List is empty")
        
        temp = self.head
        while temp:
            print(temp.data,end=("->"))
            temp = temp.next


    #def insert_b(self,data):

l = DLL()
n = Node(5)
n1 = Node(10)
n.next = n1
l.head = n


