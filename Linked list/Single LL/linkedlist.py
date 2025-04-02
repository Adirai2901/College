class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class ll:
    def __init__(self):
        self.head = None

    def insert_b(self,data):
        nd = Node(data)
        nd.next = self.head
        self.head = nd

    def insert_e(self,data):
        nd = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = nd


    def insert_p(self,pos,data):
        nd = Node(data)
        temp = self.head
        for i in range(0,pos-1):
            temp = temp.next
        nd.data = data
        nd.next = temp.next
        temp.next = nd

    
    def del_b(self):
        temp = self.head
        self.head = temp.next
        temp.next = None
    
    def del_e(self):
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None


    def del_p(self,pos):
        temp = self.head

        for i in range(1,pos-1):
            temp = temp.next
        temp.next 
        



    def display(self):
        
        if self.head is None:
            print("None")

        temp = self.head
        while temp:
            print(temp.data,end=("->"))
            temp = temp.next
        print("None")

       

       
l = ll()

l.insert_b(20)
l.insert_b(10)
l.insert_b(0)
l.insert_p(3,30)
l.insert_p(4,40)
l.insert_e(50)
l.insert_e(60)
l.insert_e(70)
l.insert_e(80)

l.del_p(4)



l.display()

