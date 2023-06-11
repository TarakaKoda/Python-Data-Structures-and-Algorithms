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
        self.items = Linked_List()

    def __str__(self):
        values = [str(node.value) for node in self.items]
        return " ".join(values)



if __name__ == "__main__":
    queue = Queue()