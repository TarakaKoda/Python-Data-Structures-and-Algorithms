class Stack:
    def __init__(self, max_value):
        self.max_value = max_value
        self.list = []

    def is_empty(self):
        if self.list == []:
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
            return "the stack is full"
        else:
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

    def __str__(self):
        if self.is_empty():
            return "stack is empty"
        elif self.list is None:
            return "stack is deleted"
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return "\n".join(values)

stack = Stack(5)

if __name__ == "__main__":
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    print(stack.push(6))
    # print(stack)
    stack.pop()
    stack.push(6)
    print(stack)
    print(stack.is_full())
    stack.delete()
    print(stack)
