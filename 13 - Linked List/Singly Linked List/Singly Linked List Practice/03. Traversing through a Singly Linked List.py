'''
Traversal
  Start -> check head -Yes-> Loop all nodes and print value -> Terminate
        -> check head -No-> Terminate
  Time - O(n) space - O(1)
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
                while index < location -1:
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = new_node
                new_node.next = next_node

    def traversing(self):
        if self.head == None:
            print("Singly Linked list does not exist")
        node = self.head
        while node:
            yield node.value
            node = node.next

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

singly_linked_list = Singly_Linked_List()

singly_linked_list.inserting(5, 0)
singly_linked_list.inserting(3, -1)
singly_linked_list.inserting(4, 1)
singly_linked_list.inserting(2, 3)
singly_linked_list.inserting(1, -1)

if __name__ == "__main__":
    print(__doc__)
    print([node.value for node in singly_linked_list])
    for i in singly_linked_list.traversing():
        if int(i)%2 == 0:
            print(i)