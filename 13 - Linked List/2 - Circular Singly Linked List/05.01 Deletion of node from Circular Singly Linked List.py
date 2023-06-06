class Linked_List:
    '''
    Delete
      - Deleting the first node Time O(1) Space O(1)
      - Deleting any given node Time O(N) space O(1)
      - Deleting the last node Time O(N) Space O(1)
      Algorithm
    '''

class Node:

    def __init__(self, value=None):
        self.value = value
        self.next = None

class Circular_Singly_Linked_List:

    def __init__(self):
        self.head = None
        self.tail = None

    def creating_circular_singly_linked_list(self, node_value):
        node = Node(node_value)
        node.next = node
        self.head = node
        self.tail = node

    def inserting(self, value, location):
        new_node = Node(value)
        if self.head is None:
            new_node = new_node.next
            self.head = new_node
            self.tail = new_node
        else:
            if location == 0:
                new_node.next = self.head
                self.head = new_node
                self.tail = new_node
            elif location == -1:
                self.tail.next = new_node
                self.tail = new_node
                new_node.next = self.head
            else:
                temp_node = self.head
                index = 0
                while index < location -1:
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = new_node
                new_node.next = next_node

    def traversing(self):
        if self.head is None:
            print("Circular Singly Linked List is empty")
        else:
            temp_node = self.head
            while temp_node:
                print(temp_node.value)
                temp_node = temp_node.next
                if temp_node == self.tail.next:
                    break

    def searching(self, value):
        if self.head is None:
            return "Circular Singly Linked List is empty"
        else:
            temp_node = self.head
            while temp_node:
                if temp_node.value == value:
                    return f"{value} found in the Circular Singly Linked List"
                temp_node = temp_node.next
                if temp_node == self.tail.next:
                    return f"{value} does not exist in the Circular Singly Linked List"

    def deletion(self, location):
        if self.head is None:
            return "Circular Singly Linked List is empty"
        else:
            if location == 0:
                if self.head == self.head.next:
                    self.head = None
                    self.tail = None
                else:
                    next_node = self.head.next
                    self.head = self.head.next
                    self.tail.next = next_node
            elif location == -1:
                if self.head == self.head.next:
                    self.head = None
                    self.tail = None
                else:
                    temp_node = self.head
                    while temp_node:
                        if temp_node.next == self.tail:
                            break
                        temp_node = temp_node.next
                    temp_node.next = self.head
                    self.tail = temp_node
            else:
                temp_node = self.head
                index = 0
                while index < location -1:
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = next_node.next

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

circular_singly_linked_list = Circular_Singly_Linked_List()

if __name__ == "__main__":
    print(Linked_List().__doc__)
    circular_singly_linked_list.creating_circular_singly_linked_list(2)
    # print([node.value for node in circular_singly_linked_list])
    circular_singly_linked_list.inserting(1,0)
    circular_singly_linked_list.inserting(3,-1)
    circular_singly_linked_list.inserting(5,0)
    circular_singly_linked_list.inserting(6,-1)
    circular_singly_linked_list.inserting(4,4)
    circular_singly_linked_list.inserting(4,-1)
    print([node.value for node in circular_singly_linked_list])
    # circular_singly_linked_list.traversing()
    # print(circular_singly_linked_list.searching(2))
    # circular_singly_linked_list.deletion(0)
    circular_singly_linked_list.deletion(1)
    circular_singly_linked_list.inserting(3,-1)
    print([node.value for node in circular_singly_linked_list])