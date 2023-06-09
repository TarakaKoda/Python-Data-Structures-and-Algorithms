'''
Implement a Recursive Algorithm to find the kth value from the last
'''
from LinkedList import Linked_List
def nth_value_from_last(linked_list, n):
    if n == 1:
        return linked_list.tail
    else:
        temp_node = linked_list.head
        while temp_node:
            if temp_node.next is linked_list.tail:
                break
            temp_node = temp_node.next
        temp_node.next = None
        linked_list.tail = temp_node
        return nth_value_from_last(linked_list, n-1)

linked_list = Linked_List()
linked_list.generate(10, 99, 1)
print(linked_list)
print(nth_value_from_last(linked_list,10))

