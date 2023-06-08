'''
Implement and Algorithm to find the nth to last element of a Singly Linked List
'''
from LinkedList import Linked_List
def find_nth_to_last(linked_list, n):
    if n > len(linked_list):
        return None
    pointer1 = linked_list.head
    pointer2 = linked_list.head

    for _ in range(n):
        if pointer2.next == None:
            return pointer1
        pointer2 = pointer2.next

    while pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1

linked_list = Linked_List()
linked_list.generate(10,99,1)

if __name__ == "__main__":
    print(__doc__)
    print(linked_list)
    print(find_nth_to_last(linked_list, 8))