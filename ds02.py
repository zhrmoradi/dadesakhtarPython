class Stack:
    def __init__(self, capacity=1000):
        self.items = []
        self.capacity = capacity

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) >= self.capacity

    def push(self, value):
        if self.is_full():
            print("Stack overflow")
            return
        self.items.append(value)

    def pop(self):
        if self.is_empty():
            print("Stack underflow")
            return None
        return self.items.pop()

    def top(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.items[-1]

    
    def find_all(self, x):
        indexes = [i for i, val in enumerate(self.items) if val == x]
        return indexes

    
    def find_first(self, x):
        for i, val in enumerate(self.items):
            if val == x:
                return i
        return -1


    def find_last(self, x):
        for i in range(len(self.items) - 1, -1, -1):
            if self.items[i] == x:
                return i
        return -1
        
    def replace(self, old, new):
        count = 0
        for i in range(len(self.items)):
            if self.items[i] == old:
                self.items[i] = new
                count += 1
        return count

s = Stack(10)
s.push(57)
s.push(126)
s.push(-10)
s.push(126)

print("Top:", s.top())
print("All indexes of 126:", s.find_all(126))
print("First index:", s.find_first(126))
print("Last index:", s.find_last(126))

s.replace(126, 999)
print("After replace:", s.items)
