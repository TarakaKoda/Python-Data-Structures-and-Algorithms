# Implement a queue using two stacks.
class Stack:
    def __init__(self):
        self.stack = []

    def __len__(self):
        return len(self.stack)

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()

class Queue:
    def __init__(self):
        self.in_queue = Stack()
        self.out_queue = Stack()

    def __str__(self):
        values = self.in_queue.stack.reverse()
        values = [str(values) for values in self.in_queue.stack]
        return " ".join(values)
    def enqueue(self, value):
        self.in_queue.push(value)

    def dequeue(self):
        if len(self.in_queue) == 0:
            return None
        else:
            while len(self.in_queue):
                self.out_queue.push(self.in_queue.pop())
            result = self.out_queue.pop()
            while len(self.out_queue):
                self.in_queue.push(self.out_queue.pop())
            return result

queue = Queue()

if __name__ == "__main__":
    queue.enqueue(5)
    queue.enqueue(2)
    queue.enqueue(6)
    print(queue)
    print(queue.dequeue())
    print(queue)





