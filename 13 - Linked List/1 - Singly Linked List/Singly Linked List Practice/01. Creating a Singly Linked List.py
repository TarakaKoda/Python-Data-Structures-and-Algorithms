'''
    Creation of Single linked lists
      - Create head and tail, initialize with null
      - Create a blank node and assign a value to it and reference to null
      - Link head and tail with these node
      Time - O(1)
      Space - O(n) based on the number of items in the linked list
'''

class Node:

    def __init__(self, value=None):
        self.value = value
        self.next = next



class Singly_Linked_List:

    def __init__(self):
        self.head = None
        self.tail = None



singly_linked_list = Singly_Linked_List()

node1 = Node(1)
node2 = Node(2)

singly_linked_list.head = node1
singly_linked_list.head.next = node2
singly_linked_list.tail = node2


if __name__ == "__main__":
    print(__doc__)
    print(singly_linked_list.head.next.value)