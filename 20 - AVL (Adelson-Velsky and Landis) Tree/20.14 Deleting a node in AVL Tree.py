from Queue import Queue
class AVL_Tree:
    def __init__(self, data):
        self.data =  data
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
        while not (queue.is_empty()):
            root = queue.dequeue()
            print(root.data)
            if root.left_child:
                queue.enqueue(root.left_child)
            if root.right_child:
                queue.enqueue(root.right_child)

def searching(root_node, value):
    if root_node is None:
        return "not found"
    elif root_node.data == value:
        return "found"
    else:
        if value < root_node.data:
            if root_node.left_child.data == value:
                return "found"
            else:
                searching(root_node.left_child, value)
        else:
            if root_node.right_child.data == value:
                return "found"
            else:
                searching(root_node.right_child, value)

# helper functions for maintaining balance after inserting new node into AVL Tree
def get_height(root_node):
    if not root_node:
        return 0
    return root_node.height

def right_rotation(disbalanced_node):
    new_root = disbalanced_node.left_child
    disbalanced_node.left_child = disbalanced_node.left_child.right_child
    new_root.right_child = disbalanced_node
    disbalanced_node.height = 1 + max(get_height(disbalanced_node.left_child), get_height(disbalanced_node.right_child))
    new_root.height = 1 + max(get_height(new_root.left_child), get_height(new_root.right_child))
    return new_root

def left_rotation(disbalanced_node):
    new_root = disbalanced_node.right_child
    disbalanced_node.right_child = disbalanced_node.right_child.left_child
    new_root.left_child = disbalanced_node
    disbalanced_node.height = 1 + max(get_height(disbalanced_node.left_child), get_height(disbalanced_node.right_child))
    new_root.height = 1 + max(get_height(new_root.left_child), get_height(new_root.right_child))
    return new_root

def get_balance(root_node):
    if not root_node:
        return 0
    else:
        return get_height(root_node.left_child) - get_height(root_node.right_child)

def insert(root_node, node_value):
    if not root_node:
        return AVL_Tree(node_value)
    elif node_value < root_node.data:
        root_node.left_child = insert(root_node.left_child, node_value)
    else:
        root_node.right_child = insert(root_node.right_child, node_value)

    root_node.height = 1 + max(get_height(root_node.left_child), get_height(root_node.right_child))
    balance = get_balance(root_node)
    if balance > 1 and node_value < root_node.left_child.data:
        return right_rotation(root_node)
    if balance > 1 and node_value > root_node.left_child.data:
        root_node.left_child = left_rotation(root_node.left_child)
        return right_rotation(root_node)
    if balance < -1 and node_value > root_node.right_child.data:
        return left_rotation(root_node)
    if balance < -1 and node_value < root_node.right_child.data:
        root_node.right_child = right_rotation(root_node.right_child)
        return left_rotation(root_node)
    return root_node

# helper function to find the successor for the root node if it has two child nodes
def min_value(root_node):
    if root_node is None:
        return root_node
    current = root_node
    while current.left_child:
        current = current.left_child
    return current

def delete(root_node, value):
    if root_node.data is None:
        return root_node
    elif value < root_node.data:
        root_node.left_child = delete(root_node.left_child, value)
    elif value > root_node.data:
        root_node.right_child = delete(root_node.right_child, value)
    else:
        if root_node.left_child is None:
            return root_node.right_child
        if root_node.right_child is None:
            return root_node.left_child

        temp = min_value(root_node.right_child)
        root_node.data = temp.data
        root_node.right_child = delete(root_node.right_child, temp.data)

        balance = get_balance(root_node)
        if balance > 1 and get_balance(root_node.left_child) >= 0:
            return right_rotation(root_node)
        if balance < -1 and get_balance(root_node.right_child) <= 0:
            return left_rotation(root_node)
        if balance > 1 and get_balance(root_node.left_child) < 0:
            root_node.left_child = left_rotation(root_node.left_child)
            return right_rotation(root_node)
        if balance < -1 and get_balance(root_node.right_child) > 0:
            root_node.right_child = right_rotation(root_node.right_child)
            return left_rotation(root_node)
        return root_node

avl_tree = AVL_Tree(5)

if __name__ == "__main__":
    avl_tree = insert(avl_tree, 10)
    avl_tree = insert(avl_tree, 20)
    avl_tree = insert(avl_tree, 40)
    avl_tree = insert(avl_tree, 50)
    avl_tree = insert(avl_tree, 60)
    avl_tree = insert(avl_tree, 80)
    delete(avl_tree, 60)
    # avl_tree = insert(avl_tree, 60)
    levelOrder_traversal(avl_tree)
