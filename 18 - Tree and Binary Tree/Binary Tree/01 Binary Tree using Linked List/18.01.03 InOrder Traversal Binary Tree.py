'''
InOder Traversal Binary Tree: Inorder traversal is a method used to visit nodes in a binary tree. In Inorder traversal,
                               the left subtree is visited first, followed by the root node, and then the right subtree.
'''

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


def preOrder_trversal(root_node):
    if not root_node:
        return
    print(root_node.data)
    preOrder_trversal(root_node.left_child)
    preOrder_trversal(root_node.right_child)

def inOrder_traversal(root_node):
    if not root_node:
        return
    inOrder_traversal(root_node.left_child)
    print(root_node.data)
    inOrder_traversal(root_node.right_child)

if __name__ == "__main__":
    print(__doc__)
    print("PreOrder Traversal")
    preOrder_trversal(root_node)
    print("\nInOrder Traversal")
    inOrder_traversal(root_node)
