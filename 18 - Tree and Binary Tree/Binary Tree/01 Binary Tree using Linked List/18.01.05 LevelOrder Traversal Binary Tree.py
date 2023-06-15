# Queue using Linked List using as a helper data structure for LevelOrders Traversal

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next  = None

    def __str__(self):
        return self.value

class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node  = self.head
        while node:
            yield node
            node = node.next

class Queue:
    def __init__(self):
        self.queue = Linked_List()

    def __str__(self):
        values = [str(node.value) for node in self.queue]
        return " ".join(values)

    def is_empty(self):
        if self.queue.head is None:
            return True
        else:
            return False

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.queue.head = new_node
            self.queue.tail = new_node
            new_node.next = None
        else:
            self.queue.tail.next = new_node
            self.queue.tail = new_node
            new_node.next = None

    def dequeue(self):
        if self.is_empty():
            return "The queue is empty"
        else:
            head_value = self.queue.head.value
            if self.queue.head == self.queue.tail:
                self.queue.head = None
                self.queue.tail = None
            else:
                self.queue.head = self.queue.head.next
            return head_value

    def peek(self):
        if self.is_empty():
            return "queue is empty"
        else:
            return self.queue.tail.value

    def delete(self):
        self.queue.head = None
        self.queue.tail = None

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
    else:
        print(root_node.data)
        preOrder_traversal(root_node.left_child)
        preOrder_traversal(root_node.right_child)

def inOrder_traversal(root_node):
    if not root_node:
        return
    else:
        inOrder_traversal(root_node.left_child)
        print(root_node.data)
        inOrder_traversal(root_node.right_child)

def postOrder_traversal(root_node):
    if not root_node:
        return
    else:
        postOrder_traversal(root_node.left_child)
        postOrder_traversal(root_node.right_child)
        print(root_node.data)

def levelOrder_travrsal(root_node):
    queue = Queue()
    queue.enqueue(root_node)
    while not (queue.is_empty()):
        root = queue.dequeue()
        print(root.data)
        if root.left_child:
            queue.enqueue(root.left_child)
        if root.right_child:
            queue.enqueue(root.right_child)


if __name__ == "__main__":
    print(__doc__)
    print("PreOrder Traversal")
    preOrder_traversal(root_node)
    print("\nInOrder Traversal")
    inOrder_traversal(root_node)
    print("\nPostOrder Traversal")
    postOrder_traversal(root_node)
    print("\nLevelOrder Traversal")
    levelOrder_travrsal(root_node)