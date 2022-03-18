class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return not self.head

    def push(self, new_node):
        new_node = Node(new_node)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def pop(self):
        if self.is_empty():
            raise Exception("The queue is empty")
        deleted_element = self.head.value
        self.head = self.head.next
        return deleted_element

    def peek(self):
        if self.is_empty():
            raise Exception("The queue is empty")
        return print(str(self.head.value))

    def __str__(self):
        node = self.head
        string = ''
        while node:
            string += str(node.value) + '<--'
            node = node.next
        return string[:-3]
