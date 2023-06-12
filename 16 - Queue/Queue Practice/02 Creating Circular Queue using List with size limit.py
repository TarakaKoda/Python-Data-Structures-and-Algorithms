class Queue:
    def __init__(self, max_value):
        self.queue = max_value * [None]
        self.max_value = max_value
        self.start = -1
        self.top = -1

    def __str__(self):
        values = [str(x) for x in self.queue]
        return " ".join(values)

    def is_empty(self):
        if self.start == -1 or self.top == -1:
            return True
        else:
            return False

    def is_full(self):
        if self.start == 0 and self.top + 1 == self.max_value:
            return True
        elif self.top + 1 == self.start:
            return True
        else:
            return False
    def enqueue(self, value):
        if self.is_full():
            return "Queue is full"
        else:
            if self.top +1 == self.max_value:
                self.top = 0
            else:
                self.top += 1
                self.start = 0
            self.queue[self.top] = value

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            first_value = self.queue[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.max_value:
                self.start = 0
            else:
                self.start += 1
            self.queue[start] = None
            return first_value
    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            return self.queue[self.start]

    def delete(self):
        self.queue = self.max_value * [None]
        self.top = -1
        self.start = -1

queue = Queue(3)

if __name__ == "__main__":
    print(queue.is_empty())
    print(queue.is_full())
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue)
    print("______")
    print(queue.peek())
    print(queue.dequeue())
    print("______")
    queue.dequeue()
    print(queue)
    queue.delete()
    print(queue)