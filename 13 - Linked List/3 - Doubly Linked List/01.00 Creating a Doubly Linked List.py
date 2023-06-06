class Linked_List:
    '''
    Doubly Linked List is same as the Singly Linked List but the only difference is each node will have two references
    previous and next. where in the Singly Linked List each node have only one reference (next)

    Creation of Circular Single linked lists
      - Create head and tail, initialize with null
      - Create a blank node and assign a value to it and references previous and next to null
      - Create a function called create_doubly_linked_list with node_value parameter
        - create a blank node using Node class
            - node = Node(node_value)
        - node.previous = null (as only one node is created the previous reference to null)
        - node.next = null (as only one node is created the next reference to null)
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

class Doubly_Linked_List:

    def __init__(self):
        self.head = None
        self.tail = None

    def create_doubly_linked_list(self, node_value):
        node = Node(node_value)
        self.head = node
        self.tail = node

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

if __name__ == "__main__":
    print(Linked_List().__doc__)
    doubly_linked_list = Doubly_Linked_List()
    doubly_linked_list.create_doubly_linked_list(2)
    print([node.value for node in doubly_linked_list])