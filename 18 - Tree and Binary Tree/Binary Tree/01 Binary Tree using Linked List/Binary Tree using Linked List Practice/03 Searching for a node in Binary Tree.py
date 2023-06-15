'''
Import queue (using Linked List data structure) as a helper function to levelOrder traversal and searching in  Binary Tree
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

if __name__ == "__main__":
    levelOrder_traversal(root_node)
    print(searching_node(root_node, "Tea"))
    print(searching_node(root_node, "Chocolate"))
