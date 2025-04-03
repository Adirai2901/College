class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self):
        x = int(input("Enter the Element: "))
        nd = Node(x)
        if self.top is None :
            self.top = nd
        else:
            nd.next = self.top
            self.top = nd
    
    def pop(self):
        if self.top is None:
            print("Stack is Empty")
        else:
            print("Popped Element: ",self.top.data)
            self.top = self.top.next
    
    def peek(self):
        if self.top is None:
            print("Stack is Empty")
        else:
            print("Top Element: ",self.top.data)
        
    def print(self):
        if self.top is None:
            print("Stack is Empty")
        else:
            temp = self.top
            while temp:
                print(temp.data,end="->")
                temp = temp.next
            print("None")
    

s = Stack()
num = int(input("Enter the number of opertaions: "))
for i in range(1, num):
    print("1-Push\n2-Pop\n3-Peak")
    x = int(input("Enter which operation: "))
    if x == 1:
        s.push()
    elif x ==2 :
        s.pop()
    elif x== 3:
        s.peek()
    else:
        print("Enter a valid operation")


    


s.print()

        