class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_last(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_after(self, target, data):
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        while current:
            if current.data == target:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        print("Not found")

    def insert_before(self, target, data):
        if self.head is None:
            print("List is empty")
            return
        if self.head.data == target:
            self.insert_first(data)
            return
        prev = None
        current = self.head
        while current:
            if current.data == target:
                new_node = Node(data)
                new_node.next = current
                prev.next = new_node
                return
            prev = current
            current = current.next
        print("Not found")

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> " if current.next else "\n")
            current = current.next
