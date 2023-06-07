class Linked_List:
    '''
    Delete entire Doubly Linked List
      - check if head?-> No terminate
        yes make head and tail = NULL
    '''

class Node:

    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.previous = None


class Circular_Doubly_Linked_List:

    def __inti__(self):
        self.head = None
        self.tail = None

    def create_circular_doubly_linked_list(self, node_value):
        node = Node(node_value)
        self.head = node
        self.tail = node
        self.next = node
        self.previous = node

    def insertion(self, value, location):
        new_node = Node(value)
        if self.head == None:
            print("Circular Doubly Linked List does not exist")
        else:
            if location == 0:
                self.head.previous = new_node
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node
            elif location == -1:
                self.tail.next = new_node
                new_node.previous = self.tail
                self.tail = new_node
                new_node.next = self.head
            else:
                temp_node = self.head
                index = 0
                while index < location - 1:
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = new_node
                new_node.previous = temp_node
                new_node.next = next_node
                next_node.previous = new_node

    def traversing(self):
        node = self.head
        while node:
            print(node.value)
            node = node.next
            if node == self.tail.next:
                break

    def reverse_traversing(self):
        node = self.tail
        while node:
            print(node.value)
            node = node.previous
            if node == self.head.previous:
                break

    def searching(self, value):
        if self.head is None:
            print("Circular Doubly Linked List does not exist")
        node = self.head
        while node:
            if node.value == value:
                return print(f"{value} found in the Circular Doubly Linked List")
            node = node.next
            if node == self.tail.next:
                break
        return print(f"{value} does not exist in the Circular Doubly Linked List")

    def delete(self, location):
        if self.head is None:
            print("Circular Doubly Linked List does not exist")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.next.previous = self.tail
                    self.tail.next = self.head
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.previous
                    self.tail.next = self.head
            else:
                temp_node = self.head
                index = 0
                while index < location -1:
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = next_node.next
                next_node.next.previous = temp_node

    def delete_entire_circular_doubly_linked_list(self):
        if self.head is None:
            print("Circular Doubly Linked List does not exist")
        else:
            self.head = None
            self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

circular_doubly_linked_list = Circular_Doubly_Linked_List()

if __name__ == "__main__":
    print(Linked_List().__doc__)
    circular_doubly_linked_list.create_circular_doubly_linked_list(2)
    circular_doubly_linked_list.insertion(1, 0)
    circular_doubly_linked_list.insertion(0, 0)
    circular_doubly_linked_list.insertion(4, -1)
    circular_doubly_linked_list.insertion(3, 3)
    print([node.value for node in circular_doubly_linked_list])
    # circular_doubly_linked_list.traversing()
    # circular_doubly_linked_list.reverse_traversing()
    # circular_doubly_linked_list.searching(4)
    circular_doubly_linked_list.delete(2)
    circular_doubly_linked_list.delete_entire_circular_doubly_linked_list()
    print([node.value for node in circular_doubly_linked_list])
    circular_doubly_linked_list.delete_entire_circular_doubly_linked_list()