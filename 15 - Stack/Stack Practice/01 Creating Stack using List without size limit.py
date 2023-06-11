class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return "\n".join(values)

    def is_empty(self):
        if self.list == []:
            return True
        else:
            return False

    def push(self, value):
        self.list.append(value)

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        else:
            return self.list.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is full"
        else:
            return self.list[-1]

    def delete(self):
        self.list = None

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(4)
stack.push(3)

if __name__ == "__main__":
    print(stack.is_empty())
    print(stack.peek())
    stack.pop()
    stack.pop()
    stack.pop()
    print(stack)
    # print(stack.pop())
    # stack.pop()
    # print(stack.peek())