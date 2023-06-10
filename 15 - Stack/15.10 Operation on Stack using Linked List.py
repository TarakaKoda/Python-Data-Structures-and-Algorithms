class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

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
        self.linked_list = Linked_List()

    def is_empty(self):
        if self.linked_list.head == None:
            return True
        else:
            return False

    def push(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.linked_list.head = new_node
            self.linked_list.head.next = None
        else:
            new_node.next = self.linked_list.head
            self.linked_list.head = new_node

    def pop(self):
        if self.is_empty():
            return "stack is empty"
        else:
            top_node = self.linked_list.head
            self.linked_list.head = self.linked_list.head.next
            return top_node.value

    def peek(self):
        if self.is_empty():
            return "stack is empty"
        return self.linked_list.head.value

    def delete(self):
        self.linked_list.head = None

    def __str__(self):
        if self.linked_list.head is None:
            return "Stack Deleted"
        values = [str(x.value) for x in self.linked_list]
        return "\n".join(values)

if __name__ == "__main__":
    stack = Stack()
    # print(stack.is_empty())
    stack.push(5)
    stack.push(4)
    stack.push(3)
    stack.push(2)
    stack.pop()
    # stack.pop()
    # stack.pop()
    print(stack)
    print(stack.peek())
    stack.delete()
    print(stack)