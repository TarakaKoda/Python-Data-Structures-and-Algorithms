class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return self.value

class Linked_List:
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

class Stack:

    def __init__(self):
        self.stack = Linked_List()

    def __str__(self):
        if self.is_empty():
            return "Stack is empty"
        values = [str(node.value) for node in self.stack]
        return "\n".join(values)

    def is_empty(self):
        if self.stack.head == None:
            return True
        else:
            return False

    def push(self, value):
        new_node = Node(value)
        if self.is_empty():
            new_node.next = None
            self.stack.head = new_node
        else:
            new_node.next = self.stack.head
            self.stack.head = new_node

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        else:
            top_node = self.stack.head
            self.stack.head = self.stack.head.next
            return top_node.value

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        else:
            return self.stack.head.value

    def delete(self):
        self.stack.head = None

stack = Stack()

if __name__ == "__main__":
    print(stack.is_empty())
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(9)
    print(stack)
    print(stack.peek())
    print(stack.pop())
    print("----")
    print(stack)
    stack.delete()
    print(stack)
