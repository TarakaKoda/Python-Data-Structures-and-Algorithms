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


def get_height(root_node):
    if not root_node:
        return 0
    return root_node.height


def right_rotate(disbalance_node):
    new_root = disbalance_node.left_child
    disbalance_node.left_child = disbalance_node.left_child.right_child
    new_root.right_child = disbalance_node
    disbalance_node.height = 1 + max(get_height(disbalance_node.left_child), get_height(disbalance_node.right_child))
    new_root.height = 1 + max(get_height(new_root.left_child), get_height(new_root.right_child))
    return new_root


def left_rotate(disbalance_node):
    new_root = disbalance_node.right_child
    disbalance_node.right_child = disbalance_node.right_child.left_child
    new_root.left_child = disbalance_node
    disbalance_node.height = 1 + max(get_height(disbalance_node.left_child), get_height(disbalance_node.right_child))
    new_root.height = 1 + max(get_height(new_root.left_child), get_height(new_root.right_child))
    return new_root


def get_balance(root_node):
    if not root_node:
        return 0
    return get_height(root_node.left_child) - get_height(root_node.right_child)


def insert_node(root_node, node_value):
    if not root_node:
        return AVL_Tree(node_value)
    elif node_value < root_node.data:
        root_node.left_child = insert_node(root_node.left_child, node_value)
    else:
        root_node.right_child = insert_node(root_node.right_child, node_value)
        
    root_node.height = 1 + max(get_height(root_node.left_child), get_height(root_node.right_child))
    balance = get_balance(root_node)
    if balance > 1 and node_value < root_node.left_child.data:
        return right_rotate(root_node)
    if balance > 1 and node_value > root_node.left_child.data:
        root_node.left_child = left_rotate(root_node.left_child)
        return right_rotate(root_node)
    if balance < -1 and node_value > root_node.right_child.data:
        return left_rotate(root_node)
    if balance < -1 and node_value < root_node.right_child.data:
        root_node.right_child = right_rotate(root_node.right_child)
        return left_rotate(root_node)
    return root_node


avl_tree = AVL_Tree(25)

if __name__ == "__main__":
    insert_node(avl_tree, 80)
    levelOrder_traversal(avl_tree)
