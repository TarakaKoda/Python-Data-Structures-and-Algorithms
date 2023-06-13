#   Create Stack with min method

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
    def __str__(self):
        string = self.value
        string += "," + str(self.next)
        return string

class Stack:
    def __init__(self):
        self.top = None
        self.min_node = None

    def min(self):
        if self.min_node is None:
            return None
        else:
            return self.min_node.value

    def push(self, value):
        if self.min_node and (self.min_node.value < value):
            self.min_node = Node(value=self.min_node.value, next=self.min_node)
        else:
            self.min_node = Node(value=value, next=self.min_node)
        self.top = Node(value=value, next=self.top)

    def pop(self):
        if self.top is None:
            return "Stack is empty"
        else:
            self.min_node = self.min_node.next
            top_value = self.top
            self.top = self.top.next
            return top_value


stack = Stack()

if __name__  == "__main__":
    print(stack.min())
    stack.push(5)
    stack.push(3)
    stack.push(2)
    print(stack.min())
    stack.pop()
    print(stack.min())