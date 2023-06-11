class Queue:
    def __init__(self, max_value):
        self.items = max_value * [None]
        self.max_value = max_value
        self.start = -1
        self.top = -1

    def __str__(self):
        if self.start == -1 and self.top  == -1:
            return "Queue is empty"
        values = [str(x) for x in self.items]
        return " ".join(values)

    def is_full(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.max_value:
            return True
        else:
            return False

    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False

    def enqueue(self, value):
        if self.is_full():
            return "Queue is full"
        else:
            if self.top + 1 == self.max_value:
                self.top = 0
            else:
                self.top += 1
                self.start = 0
            self.items[self.top] = value

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            first_element = self.items[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.max_value:
                self.start = 0
            else:
                self.start += 1
            self.items[start] = None
            return first_element

    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            return self.items[self.start]

    def delete(self):
        self.items = self.max_value * [None]
        self.top = -1
        self.start = -1

queue = Queue(3)

if __name__ == "__main__":
    print(queue.is_empty())
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.enqueue(6))
    print(queue)
    print(queue.dequeue())
    print(queue)
    print(queue.peek())
    print(queue.dequeue())
    print(queue.peek())
    queue.delete()
    print(queue)

