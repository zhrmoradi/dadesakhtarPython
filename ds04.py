class CircularQueue:
    def __init__(self, capacity=100):
        self.data = [None] * capacity
        self.capacity = capacity
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, value):
        if self.is_full():
            print("Queue is full")
            return
        if self.is_empty():
            self.front = 0
            self.rear = 0
            self.data[self.rear] = value
            return
        self.rear = (self.rear + 1) % self.capacity
        self.data[self.rear] = value

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        value = self.data[self.front]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        return value

    def show_valid(self):
        if self.is_empty():
            print("Queue is empty")
            return
        i = self.front
        while True:
            print(self.data[i])
            if i == self.rear:
                break
            i = (i + 1) % self.capacity

    def find(self, x):
        if self.is_empty():
            return None
        i = self.front
        while True:
            if self.data[i] == x:
                return i
            if i == self.rear:
                break
            i = (i + 1) % self.capacity
        return None

    def replace(self, old, new):
        if self.is_empty():
            return
        i = self.front
        while True:
            if self.data[i] == old:
                self.data[i] = new
            if i == self.rear:
                break
            i = (i + 1) % self.capacity
