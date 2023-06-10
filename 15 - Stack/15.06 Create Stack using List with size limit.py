class Stack:
    def __init__(self, max_value):
        self.max_value = max_value
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return "\n".join(values)

stack = Stack(5)
stack.list = [1,2,3,4,5]
if __name__ == "__main__":
    print(stack)