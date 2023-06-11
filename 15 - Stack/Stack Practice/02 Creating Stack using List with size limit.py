class Stack:
    def __init__(self, max_value):
        self.max_value = max_value
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return "\n".join(values)

    def is_empty(self):
        if self.list == [] or self.list == None:
            return True
        else:
            return False

    def is_full(self):
        if len(self.list) == self.max_value:
            return True
        else:
            return False

    def push(self, value):
        if self.is_full():
            return "Stack is full"
        else:
            self.list.append(value)

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        else:
            return self.list.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        else:
            return self.list[-1]

    def delete(self):
        self.list = None

stack = Stack(3)

if __name__ == "__main__":
    print(stack.is_empty())
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.is_full())
    print(stack.push(4))
    print(stack.peek())
    print("-------")
    stack.pop()
    print(stack.peek())
    print("-------")
    print(stack)