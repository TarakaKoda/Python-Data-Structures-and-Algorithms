'''
Traverse all nodes
 - PreOrder Traversal Binary Tree
 - InOrder Traversal Binary Tree
 - PostOrder Traversal Binary Tree
 - LevelOrder Traversal Binary Tree
'''
from Queue import Queue
class Binary_Search_Tree:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

def insert(root_node, value):
    if root_node.data is None:
        root_node.data = value
    elif value <= root_node.data:
        if root_node.left_child is None:
            root_node.left_child = Binary_Search_Tree(value)
        else:
            insert(root_node.left_child, value)
    else:
        if root_node.right_child is None:
            root_node.right_child = Binary_Search_Tree(value)
        else:
            insert(root_node.right_child, value)
    return "New value is successfully inserted"

# PreOder Traversal: root node -> left child -> right child
def preOder_traversal(root_node):
    if not root_node:
        return
    else:
        print(root_node.data)
        preOder_traversal(root_node.left_child)
        preOder_traversal(root_node.right_child)

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


binary_search_tree = Binary_Search_Tree(None)

if __name__ == "__main__":
    insert(binary_search_tree, 70)
    insert(binary_search_tree, 90)
    insert(binary_search_tree, 50)
    insert(binary_search_tree, 60)
    insert(binary_search_tree, 100)
    preOder_traversal(binary_search_tree)
    print("-----")
    inOrder_traversal(binary_search_tree)
    print("-----")
    postOrder_traversal(binary_search_tree)
    print("-----")
    levelOrder_traversal(binary_search_tree)