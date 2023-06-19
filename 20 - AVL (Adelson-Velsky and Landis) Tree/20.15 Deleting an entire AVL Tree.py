from Queue import Queue
class AVL_Tree:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.height = 1

def preOrder_traversal(root_node):
    if root_node is None:
        return
    else:
        print(root_node.data)
        preOrder_traversal(root_node.left_child)
        preOrder_traversal(root_node.right_child)

def inOrder_traversal(root_node):
    if root_node is None:
        return
    else:
        inOrder_traversal(root_node.left_child)
        print(root_node.data)
        inOrder_traversal(root_node.right_child)

def postOrder_traversal(root_node):
    if root_node is None:
        return
    else:
        postOrder_traversal(root_node.left_child)
        postOrder_traversal(root_node.right_child)
        print(root_node)

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
        return "not found"
    elif root_node.data == value:
        return "found"
    elif value < root_node.data:
        if root_node.left_child.data == value:
            return "found"
        else:
            searching(root_node.left_child, value)
    else:
        if root_node.right_child.data == value:
            return "found"
        else:
            searching(root_node.right_child, value)

def get_height(root_node):
    if not root_node:
        return 0
    return root_node.height

def right_rotation(disbalance_node):
    new_root = disbalance_node.left_child
    disbalance_node.left_child = disbalance_node.left_child.right_child
    new_root.right_child = disbalance_node
    disbalance_node.height = 1 + max(get_height(disbalance_node.left_child), get_height(disbalance_node.right_child))
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

def insert_node(root_node, value):
    if not root_node:
        return AVL_Tree(value)
    elif value < root_node.data:
        root_node.left_child = insert_node(root_node.left_child, value)
    else:
        root_node.right_child = insert_node(root_node.right_child, value)

    root_node.height = 1 + max(get_height(root_node.left_child), get_height(root_node.right_child))
    balance = get_balance(root_node)
    if balance > 1 and value < root_node.left_child.data:
        return right_rotation(root_node)
    if balance > 1 and value > root_node.left_child.data:
        root_node.left_child = left_rotation(root_node.left_child)
        return right_rotation(root_node)
    if balance < -1 and value > root_node.right_child.data:
        return left_rotation(root_node)
    if balance < -1 and value < root_node.right_child.data:
        root_node.right_child = right_rotation(root_node.right_child)
        return left_rotation(root_node)
    return root_node

def minimum_value(root_node):
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

        temp = minimum_value(root_node.right_child)
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

def delete_entire_avl_tree(root_node):
    root_node.data = None
    root_node.left_child = None
    root_node.right_child = None


avl_tree = AVL_Tree(25)

if __name__ == "__main__":
    avl_tree = insert_node(avl_tree, 30)
    avl_tree = insert_node(avl_tree, 40)
    avl_tree = insert_node(avl_tree, 50)
    avl_tree = insert_node(avl_tree, 60)
    avl_tree = insert_node(avl_tree, 80)
    # levelOrder_traversal(avl_tree)
    delete(avl_tree, 60)
    levelOrder_traversal(avl_tree)
