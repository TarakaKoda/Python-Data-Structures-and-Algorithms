'''
You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in
reverse order, such that the 1's digit is at head of the list. Write a function that add the two numbers and returns the
sum as a linked list
'''

from LinkedList import Linked_List


def sum_of_linked_list(linked_list1, linked_list2):
    current_node1 = linked_list1.head
    current_node2 = linked_list2.head
    carry = 0
    result_linked_list = Linked_List()

    while current_node1 or current_node2:
        result = carry
        if current_node1:
            result += current_node1.value
            current_node1 = current_node1.next

        if current_node2:
            result += current_node2.value
            current_node2 = current_node2.next

        result_linked_list.add(int(result % 10))
        carry = result/10
    return result_linked_list


llA = Linked_List()
llA.add(7)
llA.add(1)
llA.add(6)

llB = Linked_List()
llB.add(5)
llB.add(9)
llB.add(2)

if __name__ == "__main__":
    print(__doc__)
    print(llA)
    print(llB)
    print(sum_of_linked_list(llA, llB))