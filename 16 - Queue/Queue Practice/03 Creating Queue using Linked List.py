class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

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
        self.queue = Linked_List()

    def __str__(self):
        values = [str(node.value) for node in self.queue]
        return " ".join(values)

    def is_empty(self):
        if self.queue.head is None:
            return True
        else:
            return False

    def push(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.queue.head = new_node
            self.queue.tail = new_node
            new_node.next = None
        else:
            self.queue.tail.next = new_node
            self.queue.tail = new_node
            new_node.next = None

    def pop(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            top_value = self.queue.head
            self.queue.head.next = self.queue.head.next.next
            return top_value.value

    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            return self.queue.head.value

    def delete(self):
        self.queue.head = None
        self.queue.tail = None


queue = Queue()

if __name__ == "__main__":
    print(queue.is_empty())
    queue.push(1)
    queue.push(2)
    queue.push(4)
    queue.push(3)
    print(queue)
    print(queue.peek())
    print(queue.delete())
    print(queue)