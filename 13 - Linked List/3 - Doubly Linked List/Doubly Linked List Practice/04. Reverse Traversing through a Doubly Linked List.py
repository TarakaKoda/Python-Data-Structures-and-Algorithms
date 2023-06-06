class Linked_List:
    '''
    Reverse Traversal
      Start -> check head -Yes-> Loop all nodes start from tail and print value -> Terminate
            -> check head -No-> Terminate
      Time - O(n) space - O(1)
    '''

class Node:

    len = -1

    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None
        Node.len += 1


class Doubly_Linked_List:

    def __init__(self):
        self.head = None
        self.tail = None

    def create_doubly_linked_list(self, node_value):
        node = Node(node_value)
        self.head = node
        self.tail = node

    def inserting(self, value, location):
        new_node = Node(value)
        if self.head == None:
            return "Doubly Linked List does not exist"
        else:
            if location == 0:
                new_node.previous = None
                new_node.next = self.head
                self.head = new_node
            elif location >= Node.len or location == -1:
                new_node.previous = self.tail
                self.tail.next = new_node
                new_node.next = None
                self.tail = new_node
            else:
                temp_node = self.head
                index = 0
                while index < location -1:
                    temp_node = temp_node.next
                    index += 1
                new_node.next = temp_node.next
                new_node.previous = temp_node
                new_node.next.previous = new_node
                temp_node.next = new_node

    def traverse(self):
        temp_node = self.head
        while temp_node:
            print(temp_node.value)
            temp_node = temp_node.next

    def reverse_traverse(self):
        temp_node = self.tail
        while temp_node:
            print(temp_node.value)
            temp_node = temp_node.previous


    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next


doubly_linked_list = Doubly_Linked_List()

if __name__ == "__main__":
    print(Linked_List().__doc__)
    doubly_linked_list.create_doubly_linked_list(2)
    doubly_linked_list.inserting(0,0)
    doubly_linked_list.inserting(3,-1)
    doubly_linked_list.inserting(1,1)
    doubly_linked_list.inserting(4,9)
    print([node.value for node in doubly_linked_list])
    doubly_linked_list.traverse()
    print([node.value for node in doubly_linked_list])
    doubly_linked_list.reverse_traverse()