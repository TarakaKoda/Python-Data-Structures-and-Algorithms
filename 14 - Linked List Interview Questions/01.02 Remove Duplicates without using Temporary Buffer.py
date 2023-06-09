'''
Write a code to remove duplicates without using temporary in a Linked List
'''
from random import randint
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.previous = None

    def __str__(self):
        return str(self.value)

class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __str__(self):
        values = [str(node.value) for node in self]
        return "->".join(values)

    def __len__(self):
        result = 0
        temp_node = self.head
        while temp_node:
            result += 1
            temp_node = temp_node.next
        return result

    def add(self, value):
        if self.head == None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail

    def generate(self, n, max_value, min_value):
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(randint(min_value, max_value))
        return self

    @staticmethod
    def remove_duplicates_without_using_temp_buffer(linked_list):
        if linked_list.head == None:
            return
        else:
            current_node = linked_list.head
            while current_node:
                runner = current_node
                while runner.next:
                    if runner.next.value == current_node.value:
                        runner.next = runner.next.next
                    else:
                        runner = runner.next
                current_node = current_node.next
            return linked_list


linked_list = Linked_List()
linked_list.generate(5,99,1)

if __name__ == "__main__":
    print(__doc__)
    print(linked_list)
    print(linked_list.remove_duplicates_without_using_temp_buffer(linked_list))