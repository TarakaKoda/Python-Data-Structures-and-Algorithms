'''
Queue using Linked List for helper data structure for LevelOrder Traversal, searching, inserting and deleting a node in a binary tree
'''

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return self.value

class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

class Queue:
    def __init__(self):
        self.queue  = Linked_List()

    def __str__(self):
        values = [str(node.value) for node in self.queue]
        return " ".join(values)

    def is_empty(self):
        if self.queue.head is None:
            return True
        else:
            return False

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.queue.head = new_node
            self.queue.tail = new_node
        else:
            self.queue.tail.next = new_node
            self.queue.tail = new_node

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            first_value = self.queue.head.value
            if self.queue.head == self.queue.tail:
                self.queue.head = None
                self.queue.tail = None
            else:
                self.queue.head = self.queue.head.next
            return first_value

    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            return self.queue.head.value

    def delete(self):
        self.queue.head = None
        self.queue.tail = None
