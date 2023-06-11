class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        if self.is_empty() or self.items == None:
            return "Queue is empty"
        values = [str(x) for x in self.items]
        return " ".join(values)

    def is_empty(self):
        if self.items == []:
            return True
        else:
            return False

    def enqueue(self, value):
        self.items.append(value)
        return "value is inserted into the end of Queue"

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            return self.items[0]

    def delete(self):
        self.items = None

queue = Queue()

if __name__ == "__main__":
    # print(queue.is_empty())
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    print(queue)
    queue.dequeue()
    print(queue)
    print(queue.dequeue())
    print(queue)
    queue.delete()
    print(queue)
