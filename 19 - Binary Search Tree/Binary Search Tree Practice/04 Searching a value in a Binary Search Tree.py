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
    return "Successfully inserted into Binary Search Tree"

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

def searching(root_node, value):
    if root_node is None:
        print("value not found")
    elif root_node.data == value:
        print("value found")
    elif value < root_node.data:
        if root_node.left_child.data == value:
            print("value found")
        else:
            searching(root_node.left_child, value)
    else:
        if root_node.right_child.data == value:
            print("value found")
        else:
            searching(root_node.right_child, value)


binary_search_tree = Binary_Search_Tree(None)

if __name__  ==  "__main__":
    insert(binary_search_tree, 70)
    insert(binary_search_tree, 40)
    insert(binary_search_tree, 70)
    insert(binary_search_tree, 50)
    insert(binary_search_tree, 50)
    postOrder_traversal(binary_search_tree)
    searching(binary_search_tree, 50)


