'''
queue data structure using linked list as a helper class for LevelOrder Traversal and searching value in a Binary tree
For deleting an entire Binary Tree we just need create a method with root_node as argument and just need to set
the data, left_child, right_child to None. this is enough to delete an entire binary tree.
'''
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return self.value

class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
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

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            first_value = self.queue.head.value
            if self.queue.head == self.queue.tail:
                self.queue.head = None
                self.queue.tail = None
            else:
                self.queue.head = self.queue.head.next
            return first_value

    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            return self.queue.head

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

new_node = Binary_Tree("Biscuit")

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

def levelOrder_traversal(root_node):
    if not root_node:
        return "Binary Tree does not exist"
    queue = Queue()
    queue.enqueue(root_node)
    while not queue.is_empty():
        root = queue.dequeue()
        print(root.data)
        if root.left_child is not None:
            queue.enqueue(root.left_child)
        if root.right_child is not None:
            queue.enqueue(root.right_child)

def searching_value(root_node, value):
    if not root_node:
        return
    queue = Queue()
    queue.enqueue(root_node)
    while not queue.is_empty():
        root = queue.dequeue()
        if root.data == value:
            return "Success"
        if root.left_child:
            queue.enqueue(root.left_child)
        if root.right_child:
            queue.enqueue(root.right_child)
    return f"{value} does not exist in the Binary Tree"

def inserting_node(root_node, new_node):
    if not root_node:
        root_node.data = new_node
    else:
        queue = Queue()
        queue.enqueue(root_node)
        while not queue.is_empty():
            root = queue.dequeue()
            if root.left_child is not None:
                queue.enqueue(root.left_child)
            else:
                root.left_child = new_node
                return "New node has been added"
            if root.right_child is not None:
                queue.enqueue(root.right_child)
            else:
                root_node.right_child = new_node
                return "New node has been added"

def find_deepest_node(root_node):
    if not root_node:
        return
    else:
        queue = Queue()
        queue.enqueue(root_node)
        while not queue.is_empty():
            root = queue.dequeue()
            if root.left_child:
                queue.enqueue(root.left_child)
            if root.right_child:
                queue.enqueue(root.right_child)
        deepest_value = root
        return deepest_value

def delete_deepest_node(root_node, deepest_node):
    if not root_node:
        return
    else:
        queue = Queue()
        queue.enqueue(root_node)
        while not queue.is_empty():
            root = queue.dequeue()
            if root is deepest_node:
                root = None
                return
            if root.right_child:
                if root.right_child is deepest_node:
                    root.right_child = None
                    return
                else:
                    queue.enqueue(root.right_child)
            if root.left_child:
                if root.left_child is deepest_node:
                    root.left_child = None
                    return
                else:
                    queue.enqueue(root.left_child)

def deleting_node(root_node, node):
    if not root_node:
        return
    else:
        queue = Queue()
        queue.enqueue(root_node)
        while not queue.is_empty():
            root = queue.dequeue()
            if root.data == node:
                last_node = find_deepest_node(root_node)
                root.data = last_node.data
                delete_deepest_node(root_node, last_node)
                return "Node has been successfully deleted"
            if root.left_child:
                queue.enqueue(root.left_child)
            if root.right_child:
                queue.enqueue(root.right_child)

def delete_entire_binary_tree(root_node):
    root_node.data = None
    root_node.left_child = None
    root_node.right_child = None
    return "Binary Tree has been deleted"

if __name__ == "__main__":
    print(__doc__)
    # print("PreOrder Traversal")
    # preOrder_traversal(root_node)
    # print("\nInOrder Traversal")
    # inOrder_traversal(root_node)
    # print("\nPostOrder Traversal")
    # postOrder_traversal(root_node)
    # print("\nLevelOrder Traversal")
    # levelOrder_traversal(root_node)
    # print(searching_value(root_node, "Cola"))
    # print(searching_value(root_node, "biscuit"))

    # print(inserting_node(root_node, new_node))
    # print("\nLevelOrder Traversal")
    # levelOrder_traversal(root_node)
    # d_node = find_deepest_node(root_node)
    # # print(d_node)
    # delete_deepest_node(root_node, d_node)
    # print("       ")
    # levelOrder_traversal(root_node)
    # print(deleting_node(root_node,"Tea"))
    # levelOrder_traversal(root_node)
    print(delete_entire_binary_tree(root_node))
    levelOrder_traversal(root_node)

