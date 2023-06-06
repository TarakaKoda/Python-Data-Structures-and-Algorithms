class Linked_List:
    '''
    Circular Singly Linked List is same as the Singly Linked List but the only difference is the last node will have the
    reference to the first node. where in the Singly Linked List the last node reference to NULL (None)

    Creation of Circular Single linked lists
      - Create head and tail, initialize with null
      - Create a blank node and assign a value to it and reference to null
      - Create a function called create_circular_singly_linked_list with node_value parameter
        - create a blank node using Node class
            - node = Node(node_value)
        - node.next = node (as only one node is created the reference to that node is itself as it is the first and last node)
        - Link head and tail with these node
            - head = node
            - tail = node
      Time - O(1)
      Space - O(n) based on the number of items in the linked list
    '''

class Node:

    def __init__(self, value=None):
        self.value = value
        self.next = None


class Circular_Singly_Linked_List:

    def __init__(self):
        self.head = None
        self.tail = None


    def create_circular_singly_linked_list(self, node_value):
        node = Node(node_value)
        node.next = node
        self.head = node
        self.tail = node

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next

circular_singly_linked_list = Circular_Singly_Linked_List()

if __name__ == "__main__":
    print(Linked_List().__doc__)
    # circular_singly_linked_list.create_circular_singly_linked_list(2)
    # print([node.value for node in circular_singly_linked_list])



