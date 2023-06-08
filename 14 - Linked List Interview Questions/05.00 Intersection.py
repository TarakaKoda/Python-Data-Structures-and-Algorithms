'''
Intersection of two linked list
'''

from LinkedList import Linked_List, Node


def intersection(llA, llB):
    if llA.tail is not llB.tail:
        return False

    lenA = len(llA)
    lenB = len(llB)

    shorter = llA if lenA < lenB else llB
    longer = llB if lenA < lenB else llA

    diff = len(longer) - len(shorter)
    longerNode = longer.head
    shorterNode = shorter.head

    for i in range(diff):
        longerNode = longerNode.next

    while shorterNode is not longerNode:
        shorterNode = shorterNode.next
        longerNode = longerNode.next

    return longerNode


# Helper addition method
def addSameNode(llA, llB, value):
    tempNode = Node(value)
    llA.tail.next = tempNode
    llA.tail = tempNode
    llB.tail.next = tempNode
    llB.tail = tempNode


llA = Linked_List()
llA.generate(3, 10, 0)

llB = Linked_List()
llB.generate(4, 10, 0)

addSameNode(llA, llB, 11)
addSameNode(llA, llB, 14)

if __name__ == "__main__":
    print(__doc__)
    print(llA)
    print(llB)
    print(intersection(llA, llB))