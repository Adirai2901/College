class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self,item):
        self.queue.append(item)
        print(f"Enqueued: {item}")
    
    def is_empty(self):
        return len(self.queue) == 0

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")

        item = self.queue.pop(0)
        print(f"Dequeueed: {item}")

    def peek(self):
        if self.is_empty():
            print("Queue is empty")

        print(f"Front of the queue{self.queue[0]}")
        
        