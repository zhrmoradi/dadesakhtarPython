class SimpleQueue:
    def __init__(self, capacity=100):
        self.data = [None] * capacity
        self.capacity = capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, value):
        if self.is_full():
            print("Queue is full")
            return

        self.rear += 1
        self.data[self.rear] = value
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None

        value = self.data[self.front]
        self.front += 1
        self.size -= 1
        return value


q = SimpleQueue(3)
q.enqueue(57)
q.enqueue(32)
q.enqueue(44)
q.enqueue(39)

print(q.dequeue())
q.enqueue(39)


class CircularQueue:
    def __init__(self, capacity):
        self.data = [None] * capacity
        self.capacity = capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, value):
        if self.is_full():
            print("Circular Queue is full")
            return

        self.rear = (self.rear + 1) % self.capacity
        self.data[self.rear] = value
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            print("Circular Queue is
