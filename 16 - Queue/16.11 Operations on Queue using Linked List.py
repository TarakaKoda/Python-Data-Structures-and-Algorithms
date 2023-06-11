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
            node =  node.next


class Queue:
    def __init__(self):
        self.items = Linked_List()

    def __str__(self):
        if self.is_empty():
            return "Queue is empty"
        values = [str(node.value) for node in self.items]
        return " ".join(values)

    def is_empty(self):
        if self.items.head == None:
            return True
        else:
            return False

    def enqueue(self, value):
        new_node = Node(value)
        if self.items.head == None:
            self.items.head = new_node
            self.items.tail  = new_node
            new_node.next = None
        else:
            self.items.tail.next = new_node
            self.items.tail = new_node

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            first_value = self.items.head.value
            if self.items.head == self.items.tail:
                self.items.head = None
                self.items.tail = None
            else:
                self.items.head = self.items.head.next
            return first_value

    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            return self.items.head.value

    def delete(self):
        self.items.head = None
        self.items.tail = None

queue = Queue()

if __name__ == "__main__":
    print(queue.is_empty())
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.peek())
    queue.enqueue(4)
    queue.enqueue(5)
    print(queue)
    queue.dequeue()
    queue.dequeue()
    print(queue.peek())
    queue.dequeue()
    print(queue.peek())
    queue.delete()
    print(queue)