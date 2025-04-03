class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued: {item}")

    def is_empty(self):
        return len(self.queue) == 0
    
    
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        item = self.queue.pop(0)
        print(f"Dequeued: {item}")

  
    def peek(self):
        if self.is_empty():
            print("Queue is empty. Nothing to peek.")
            return None
        print(f"Front of the queue: {self.queue[0]}")


q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.peek()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()