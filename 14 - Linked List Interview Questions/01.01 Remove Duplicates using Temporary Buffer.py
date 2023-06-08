'''
Write a code to remove duplicate from given Linked List
'''
from LinkedList import Linked_List

def remove_duplicate(linked_list):
    if linked_list.head is None:
        return
    else:
        current_node = linked_list.head
        unique_linked_list = {current_node.value}
        while current_node.next:
            if current_node.next.value in unique_linked_list:
                current_node.next = current_node.next.next
            else:
                unique_linked_list.add(current_node.next.value)
                current_node = current_node.next
        return linked_list


custom_linked_list = Linked_List()
custom_linked_list.generate(10, 99,0)

if __name__ == "__main__":
    print(__doc__)
    print(custom_linked_list)
    print(remove_duplicate(custom_linked_list))