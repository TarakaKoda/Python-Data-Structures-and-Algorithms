class Queue:
    def __init__(self):
        self.queue = []

    def __str__(self):
        if self.is_empty():
            return "queue is empty"
        elif self.queue == None:
            return "queue is deleted"
        else:
            values = [str(x) for x in self.queue]
            return " ".join(values)

    def is_empty(self):
        if self.queue == []:
            return True
        else:
            return False

    def push(self, value):
        self.queue.append(value)

    def pop(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            return self.queue[0]

    def delete(self):
        self.queue = None

queue = Queue()

if __name__ == "__main__":
    print(queue.is_empty())
    queue.push(1)
    queue.push(2)
    queue.push(3)
    queue.push(4)
    print(queue)
    print(queue.pop())
    print(queue.peek())
    print(queue)
    print(queue.pop())
    queue.pop()
    queue.pop()
    print(queue)
    queue.delete()
    print(queue)