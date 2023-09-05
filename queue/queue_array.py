class Queue:
    def __init__(self, size):
        self.size = size
        self.data = []
        self.top = -1

    def enqueue(self, data):
        if self.top == -1:
            # indicates queue is empty
            self.data.append(data)
        else:
            # queue is not empty
            self.data.insert(0, data)
        
        self.top = self.top + 1
        self.size = self.size + 1
    
    def dequeue(self):
        dequeued_data = self.data[0]
        if dequeued_data:
            self.data.pop(0)
            self.size = self.size - 1
            self.top = self.top - 1
            return dequeued_data
        else:
            print("Queue is empty.")
            return


queue = Queue(5)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.data[0: queue.size])

queue.dequeue()

print(queue.data[0: queue.size])
