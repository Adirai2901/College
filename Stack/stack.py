
# def push(val):
#     stack =[]
#     stack.append(val)
#     return stack



# x = int(input("Enter the number of numbers"))
# for i in range(0,x) :
#     val = int(input("Enter the Element: "))
#     print(push(val))




# # stack=[]
# # stack.append(1)
# # stack.append(2)
# # stack.append(3)
# # stack.append(4)

# # print(stack)
# # print(stack.pop())
# # print(stack.pop())
# # print(stack[-1])
# # size = len(stack)==0
# # print(size)

class Stack:
    def __init__(self):
        self.item = []

    def push(self,val):
        self.item.append(val)

    def pop(self):
        if len(self.item)!=0:
             print("Poped item: ",self.item.pop())

    def peak(self):
        print( "Top element: ",self.item[-1])


    def print(self):
        if len(self.item)==0:
            print("Stack underflow")
        print(self.item)


s = Stack()

s.push(5)
s.push(10)
s.push(20)
s.push(5)
s.push(10)
s.push(20)
s.print()
s.peak()
s.pop()
s.print()