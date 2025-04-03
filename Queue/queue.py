class Queue:
    def __init__(self):
        self.queue = []

    
    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued: {item}")

    
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        item = self.queue.pop(0)
        print(f"Dequeued: {item}")
        return item

  
    def peek(self):
        if self.is_empty():
            print("Queue is empty. Nothing to peek.")
            return None
        print(f"Front of the queue: {self.queue[0]}")
        return self.queue[0]

    
    def is_empty(self):
        return len(self.queue) == 0

   
    def size(self):
        print(f"Queue size: {len(self.queue)}")
        return len(self.queue)


if __name__ == "__main__":
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.peek()
    q.size()
    q.dequeue()
    q.size()
    q.dequeue()
    q.dequeue()
    q.dequeue()