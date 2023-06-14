'''
PreOder Traversal Binary Tree: Preorder traversal is a method used to visit nodes in a binary tree. In preorder traversal,
                               the root node is visited first, followed by the left subtree, and then the right subtree.
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
left_child = Binary_Tree("Hot")
right_child = Binary_Tree("Cold")

# root_node.left_child = left_child
# root_node.right_child = right_child

root_node.add_children(left_child, right_child)



def preorder_traversal(root_node):
    if root_node is None:
        return
    print(root_node.data)
    preorder_traversal(root_node.left_child)
    preorder_traversal(root_node.right_child)


if __name__ == "__main__":
    print(__doc__)
    preorder_traversal(root_node)