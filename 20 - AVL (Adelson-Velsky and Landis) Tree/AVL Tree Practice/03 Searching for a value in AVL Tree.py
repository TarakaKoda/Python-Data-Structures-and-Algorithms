from Queue import Queue
class AVL_Tree:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.height = 1

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
        return "value not found"
    elif root_node.data == value:
        return "Found"
    elif value <= root_node.data:
        if root_node.left_child == value:
            return "Found"
        else:
            searching(root_node.left_child, value)
    else:
        if root_node.right_child == value:
            return "Found"
        else:
            searching(root_node.right_child, value)

avl_tree = AVL_Tree(50)

if __name__ == "__main__":
    print(searching(avl_tree, 50))
