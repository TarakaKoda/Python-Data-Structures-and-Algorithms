'''
Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x.
'''

from LinkedList import Linked_List


def partition(linked_list, value):
    if linked_list.head is None:
        return None
    else:
        current_node = linked_list.head
        linked_list.tail = linked_list.head

        while current_node:
            next_node = current_node.next
            current_node.next = None
            if current_node.value < value:
                current_node.next = linked_list.head
                linked_list.head = current_node
            else:
                linked_list.tail.next = current_node
                linked_list.tail = current_node
            current_node = next_node
        if linked_list.tail.next:
            linked_list.tail.next = None
        return linked_list

customLL = Linked_List()
customLL.generate(10, 99, 0)

if __name__ == "__main__":
    print(__doc__)
    print(customLL)
    partition(customLL, 30)
    print(customLL)