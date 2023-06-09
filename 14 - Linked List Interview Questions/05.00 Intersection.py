'''
Intersection of two linked list
'''

from LinkedList import Linked_List, Node


def intersection(linked_list1, linked_list2):
    if linked_list1.tail is not linked_list2.tail:
        return False

    ll1 = len(linked_list1)
    ll2 = len(linked_list2)

    shorter = linked_list1 if ll1 < ll2 else linked_list2
    longer = linked_list2 if ll1 < ll2 else linked_list1

    difference = len(longer) - len(shorter)

    longer_node = longer.head
    shorter_node = shorter.head

    for _ in range(difference):
        longer_node = longer_node.next

    while shorter_node is not longer_node:
        shorter_node = shorter_node.next
        longer_node = longer_node.next
    return longer_node



# Helper addition method
def adding_insertion_between_linked_list(linked_list1, linked_list2, value):
    new_node = Node(value)
    linked_list1.tail.next = new_node
    linked_list1.tail = new_node
    linked_list2.tail.next = new_node
    linked_list2.tail = new_node


llA = Linked_List()
llA.generate(3, 10, 0)

llB = Linked_List()
llB.generate(4, 10, 0)

adding_insertion_between_linked_list(llA, llB, 11)
adding_insertion_between_linked_list(llA, llB, 14)

if __name__ == "__main__":
    print(__doc__)
    print(llA)
    print(llB)
    print(intersection(llA, llB))