class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_first(self, data):
        new_node = DNode(data)
        if self.head is None:
            self.head = self.tail = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insert_last(self, data):
        if self.head is None:
            self.insert_first(data)
            return
        new_node = DNode(data)
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def insert_after(self, target, data):
        current = self.head
        while current:
            if current.data == target:
                if current == self.tail:
                    self.insert_last(data)
                    return True
                new_node = DNode(data)
                new_node.next = current.next
                new_node.prev = current
                current.next.prev = new_node
                current.next = new_node
                return True
            current = current.next
        return False

    def insert_before(self, target, data):
        current = self.head
        while current:
            if current.data == target:
                if current == self.head:
                    self.insert_first(data)
                    return True
                new_node = DNode(data)
                new_node.next = current
                new_node.prev = current.prev
                current.prev.next = new_node
                current.prev = new_node
                return True
            current = current.next
        return False

    def delete_first(self):
        if self.head is None:
            return False
        temp = self.head
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        del temp
        return True

    def delete_last(self):
        if self.tail is None:
            return False
        if self.head == self.tail:
            return self.delete_first()
        temp = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        del temp
        return True

    def delete_before(self, target):
        current = self.head
        while current:
            if current.data == target:
                if current.prev is None:
                    return False
                temp = current.prev
                if temp.prev:
                    temp.prev.next = current
                    current.prev = temp.prev
                else:
                    current.prev = None
                    self.head = current
                del temp
                return True
            current = current.next
        return False

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> " if current.next else "\n")
            current = current.next
