'''
Import queue (using Linked List data structure) as a helper function to levelOrder traversal, searching, inserting
and deleting in  Binary Tree.
For Deleting a node in Binary Tree we need 2 helper function: 1. Finding the deepest node, 2. Deleting the deepest node
Use this 2 helper function in a deleting a specific node in Binary Tree
'''
from Queue import Queue


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
right_hot_node = Binary_Tree("Coffee")

left_node.add_children(left_hot_node, right_hot_node)

left_cold_node = Binary_Tree("Soda")
right_cold_node = Binary_Tree("Cola")

right_node.add_children(left_cold_node, right_cold_node)


# PreOder Traversal: root node -> left child -> right child
def preOrder_traversal(root_node):
    if not root_node:
        return
    else:
        print(root_node.data)
        preOrder_traversal(root_node.left_child)
        preOrder_traversal(root_node.right_child)

# InOrder Traversal: left child -> root node -> right child
def inOrder_traversal(root_node):
    if not root_node:
        return
    else:
        inOrder_traversal(root_node.left_child)
        print(root_node.data)
        inOrder_traversal(root_node.right_child)

# PostOrder Traversal: left child -> right child -> root node
def postOrder_traversal(root_node):
    if not root_node:
        return
    else:
        postOrder_traversal(root_node.left_child)
        postOrder_traversal(root_node.right_child)
        print(root_node.data)

# LevelOrder Traversal: we visit all nodes at a given level before moving to the next level.
def levelOrder_traversal(root_node):
    if not root_node:
        return
    else:
        queue = Queue()
        queue.enqueue(root_node)
        while not queue.is_empty():
            root = queue.dequeue()
            print(root.data)
            if root.left_child:
                queue.enqueue(root.left_child)
            if root.right_child:
                queue.enqueue(root.right_child)

def searching_node(root_node, value):
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
    return f"{value} does not exit in the Binary Tree"

def insert_node(root_node, node):
    if not root_node:
        root_node.data = node
        return "New node inserted"
    else:
        queue = Queue()
        queue.enqueue(root_node)
        while not queue.is_empty():
            root = queue.dequeue()
            if root.left_child:
                queue.enqueue(root.left_child)
            else:
                root.left_child = node
                return "New node has been inserted"
            if root.right_child:
                queue.enqueue(root.right_child)
            else:
                root.right_child = node
                return "New node has been inserted"

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
        deepest_node = root
        return deepest_node

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

def delete_node(root_node, value):
    if not root_node:
        return
    else:
        queue = Queue()
        queue.enqueue(root_node)
        while not queue.is_empty():
            root = queue.dequeue()
            if root.data == value:
                last_node = find_deepest_node(root_node)
                root.data = last_node.data
                delete_deepest_node(root_node, last_node)
                return "Successfully deleted"
            if root.left_child:
                queue.enqueue(root.left_child)
            if root.right_child:
                queue.enqueue(root.right_child)



if __name__ == "__main__":
    levelOrder_traversal(root_node)
    # deepest_node = find_deepest_node(root_node)
    # delete_deepest_node(root_node, deepest_node)
    # print("  ")
    # levelOrder_traversal(root_node)
    delete_node(root_node, "Tea")
    levelOrder_traversal(root_node)



