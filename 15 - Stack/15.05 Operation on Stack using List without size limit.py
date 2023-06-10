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
            return "stack is empty"
        else:
            return self.list.pop()

    def peek(self):
        if self.is_empty():
            return "stack is empty"
        else:
            return self.list[-1]

    def delete(self):
        self.list = None

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
if __name__ == "__main__":
    # print(stack.pop())
    # print("")
    # print(stack.is_empty())
    print(stack.peek())
    # print(stack)
    # stack.delete()
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack)


