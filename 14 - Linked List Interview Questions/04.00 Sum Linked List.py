'''
You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in
reverse order, such that the 1's digit is at head of the list. Write a function that add the two numbers and returns the
sum as a linked list
'''

from LinkedList import Linked_List


def sumList(llA, llB):
    n1 = llA.head
    n2 = llB.head
    carry = 0
    ll = Linked_List()

    while n1 or n2:
        result = carry
        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next
        ll.add(int(result % 10))
        carry = result / 10

    return ll


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
    print(sumList(llA, llB))