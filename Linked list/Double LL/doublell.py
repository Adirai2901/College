class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

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
        print("None")


    def insert_b(self,data):
        nd = Node(data)
        # temp = self.head
        # temp.prev = nd
        # nd.next = temp
        # self.head = nd

        temp = self.head
        nd.next = self.head
        self.head = nd
        
    def insert_e(self,data):
        nd = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = nd
        nd.prev = temp


l = DLL()
# n = Node(5)
# n1 = Node(10)
# n2 = Node(20)
# n.next=n1
# n1.prev=n
# n2.prev = n1
# n1.next = n2
# l.head = n

l.insert_b(5)
l.insert_b(10)
l.insert_b(20)

l.insert_e(30)
l.display()


