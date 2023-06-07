class Linked_List:
    '''
    Circular Doubly Linked List is same as the Doubly Linked List but the only difference is the first and last node will have two references
    previous and next to each other. where in the Doubly Linked List first node previous node is null and last node next reference is null

    Creation of Circular Doubly Linked Lists
      - Create head and tail, initialize with null
      - Create a blank node and assign a value to it and references previous and next to null
      - Create a function called create_circular_doubly_linked_list with node_value parameter
        - create a blank node using Node class
            - node = Node(node_value)
        - node.previous = node (as only one node is created the previous reference to itself)
        - node.next = node (as only one node is created the next reference to itself)
        - Link head and tail with the node
            - head = node
            - tail = node
      Time - O(1)
      Space - O(n) based on the number of items in the linked list
    '''

class Node:

    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.previous = None

class Circular_Doubly_Linked_List:

    def __init__(self):
        self.head = None
        self.tail = None

    def create_circular_doubly_linked_list(self, node_value):
        node = Node(node_value)
        self.next = node
        self.previous = node
        self.head = node
        self.tail = node

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
    print([node.value for node in circular_doubly_linked_list])
