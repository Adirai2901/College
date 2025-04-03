class FS:
    def __init__(self,size):
        self.stack =[0]*size
        self.top =-1
        self.size = size
    
    def is_full(self):
        return self.top == self.size
    def is_empty(self):
        return self.top ==-1

    def push(self,data):
        if self.is_full():
            print("Stack overflow")
        else:
            self.top +=1
            self.stack[self.top] = data


        