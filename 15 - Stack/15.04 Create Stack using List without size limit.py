class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return "\n".join(values)


stack = Stack()
stack.list = [1,2,3,4,5]


if __name__ == "__main__":
    print(stack)