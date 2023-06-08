'''
Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x.
'''

from LinkedList import Linked_List


def partition(ll, x):
    curNode = ll.head
    ll.tail = ll.head

    while curNode:
        nextNode = curNode.next
        curNode.next = None
        if curNode.value < x:
            curNode.next = ll.head
            ll.head = curNode
        else:
            ll.tail.next = curNode
            ll.tail = curNode
        curNode = nextNode

    if ll.tail.next is not None:
        ll.tail.next = None


customLL = Linked_List()
customLL.generate(10, 99, 0)

if __name__ == "__main__":
    print(__doc__)
    print(customLL)
    partition(customLL, 30)
    print(customLL)