



from Queue import Queue
class Binary_Search_Tree:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

def insert(root_node, value):
    if root_node.data is None:
        root_node.data = value
    else:
        if value <= root_node.data:
            if root_node.left_child is None:
                root_node.left_child = Binary_Search_Tree(value)
            else:
                insert(root_node.left_child, value)
        else:
            if root_node.right_child is None:
                root_node.right_child = Binary_Search_Tree(value)
            else:
                insert(root_node.right_child, value)
    return "value successfully inserted"

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
                queue.enqueue((root.right_child))

def searching(root_node, value):
    if root_node is None:
        print("value does not exist")
    elif root_node.data == value:
        print("Found")
    elif value < root_node.data:
        if root_node.left_child == value:
            print("Found")
        else:
            searching(root_node.left_child, value)
    else:
        if root_node.right_child == value:
            print("Found")
        else:
            searching(root_node.right_child, value)

def minimum_value(binary_search_tree):
    current = binary_search_tree
    while current.left_child is not None:
        current = current.left_child
    return current

def delete_node(root_node, value):
    if root_node is None:
        return None
    elif value < root_node.data:
        root_node.left_child = delete_node(root_node.left_child, value)
    elif value > root_node.data:
        root_node.right_child = delete_node(root_node.right_child, value)
    else:
        if root_node.left_child is None:
            temp = root_node.right_child
            root_node = None
            return temp
        if root_node.right_child is None:
            temp = root_node.left_child
            root_node = None
            return temp

        temp = minimum_value(root_node.right_child)
        root_node.data = temp.data
        root_node.right_child = delete_node(root_node.right_child, temp.data)
    return root_node

def delete_entire_binary_search_tree(binary_search_tree):
    binary_search_tree.data = None
    binary_search_tree.left_child = None
    binary_search_tree.right_child = None

binary_search_tree = Binary_Search_Tree(None)

if __name__ == "__main__":
    insert(binary_search_tree, 50)
    insert(binary_search_tree, 60)
    insert(binary_search_tree, 40)
    insert(binary_search_tree, 30)
    insert(binary_search_tree, 80)
    levelOrder_traversal(binary_search_tree)
    delete_node(binary_search_tree, 40)
    levelOrder_traversal(binary_search_tree)
    delete_entire_binary_search_tree(binary_search_tree)
    levelOrder_traversal(binary_search_tree)









