'''
    Insertion to linked list
      - At the beginning of the linked list Time - O(1) space - O(1)
      - After a node in the middle of linked list Time - O(n) space - O(1)
      - At the end of the linked list Time - O(1) space - O(1)
'''
class Node:

    def __init__(self, value=None):
        self.value = value
        self.next = None


class Singly_Linked_List:

    def __init__(self):
        self.head = None
        self.tail =None

    def inserting(self, value, location):
        new_node = Node(value)
        # if Singly Linked List is empty
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            # Inserting at the beginning of the Singly Linked List
            if location == 0:
                new_node.next = self.head
                self.head = new_node
            # Inserting at the end of the Singly Linked List
            elif location == -1:
                new_node.next = None
                self.tail.next = new_node
                self.tail = new_node
            # Inserting at a specific location of the Singly Linked List
            else:
                temp_node = self.head
                index = 0
                while index < location -1:
                    temp_node = temp_node.next
                    index +=1
                next_node = temp_node.next
                temp_node.next = new_node
                new_node.next = next_node

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next


singly_linked_list = Singly_Linked_List()

singly_linked_list.inserting(0, 0)
singly_linked_list.inserting(2, -1)
singly_linked_list.inserting(1, 1)
singly_linked_list.inserting(3, 3)


if __name__ == "__main__":
    print(__doc__)
    print([node.value for node in singly_linked_list])
