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

class Singly_Linked_List:

    def __init__(self):
        self.head = None
        self.tail = None

    def inserting(self, value, location):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            if location == 0:
                new_node.next = self.head
                self.head = new_node
            elif location == -1:
                new_node.next = None
                self.tail.next = new_node
                self.tail = new_node
            else:
                temp_node = self.head
                index = 0
                while index < location - 1:
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = new_node
                new_node.next = next_node

    def traversing(self):
        if self.head == None:
            print("Singly Linked List does not exist")
        else:
            node = self.head
            while node:
                print(node.value)
                node = node.next

    def searching(self, value):
        if self.head == None:
            return "Singly Linked List does not exist"
        else:
            node = self.head
            while node:
                if node.value == value:
                    return f"value {value} found in Singly Linked List"
                else:
                    node = node.next

            return f"value {value} does not exist in Singly Linked List"

    # Delete a node from Singly Linked List
    def deletion(self, location):
        if self.head is None:
            return "The Singly Linked List does not exist"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

singly_linked_list = Singly_Linked_List()

singly_linked_list.inserting(2, 0)
singly_linked_list.inserting(3, -1)
singly_linked_list.inserting(4, -1)
singly_linked_list.inserting(1, 2)
singly_linked_list.inserting(1, 3)
singly_linked_list.inserting(3, 4)
singly_linked_list.inserting(2, 1)

if __name__ == "__main__":
    print(Linked_List().__doc__)
    print([node.value for node in singly_linked_list])
    print(singly_linked_list.searching(9))



