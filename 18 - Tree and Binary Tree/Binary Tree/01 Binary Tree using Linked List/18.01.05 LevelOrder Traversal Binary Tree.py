# Queue using Linked List
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next


class Queue:
    def __init__(self):
        self.linkedList = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.linkedList]
        return ' '.join(values)

    def enqueue(self, value):
        newNode = Node(value)
        if self.linkedList.head == None:
            self.linkedList.head = newNode
            self.linkedList.tail = newNode
        else:
            self.linkedList.tail.next = newNode
            self.linkedList.tail = newNode

    def is_empty(self):
        if self.linkedList.head == None:
            return True
        else:
            return False

    def dequeue(self):
        if self.is_empty():
            return "There is not any node in the Queue"
        else:
            tempNode = self.linkedList.head
            if self.linkedList.head == self.linkedList.tail:
                self.linkedList.head = None
                self.linkedList.tail = None
            else:
                self.linkedList.head = self.linkedList.head.next
            return tempNode

    def peek(self):
        if self.is_empty():
            return "There is not any node in the Queue"
        else:
            return self.linkedList.head

    def delete(self):
        self.linkedList.head = None
        self.linkedList.tail = None


class Binary_Tree:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def add_children(self, left_child, right_child):
        self.left_child = left_child
        self.right_child = right_child

root_node = Binary_Tree("Drinks")
left_node = Binary_Tree("Hot")
right_node = Binary_Tree("Cold")

root_node.add_children(left_node, right_node)

left_hot_node = Binary_Tree("Tea")
right_hot_node =Binary_Tree("Coffee")

left_node.add_children(left_hot_node, right_hot_node)

left_cold_node = Binary_Tree("Soda")
right_cold_node = Binary_Tree("Cola")

right_node.add_children(left_cold_node, right_cold_node)

def preOrder_traversal(root_node):
    if not root_node:
        return
    print(root_node.data)
    preOrder_traversal(root_node.left_child)
    preOrder_traversal(root_node.right_child)

def inOrder_traversal(root_node):
    if not root_node:
        return
    preOrder_traversal(root_node.left_child)
    print(root_node.data)
    preOrder_traversal(root_node.right_child)

def postOrder_traversal(root_node):
    if not root_node:
        return
    preOrder_traversal(root_node.left_child)
    preOrder_traversal(root_node.right_child)
    print(root_node.data)


def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.is_empty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)

            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)

if __name__ == "__main__":
    print(__doc__)
    print("PreOrder Traversal")
    preOrder_traversal(root_node)
    print("\nInOrder Traversal")
    inOrder_traversal(root_node)
    print("\nPostOrder Traversal")
    postOrder_traversal(root_node)
    print("Level Order Traversal")
    levelOrderTraversal(root_node)