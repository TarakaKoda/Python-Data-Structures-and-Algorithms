'''
PostOrder Traversal Binary Tree: PostOrder Traversal Binary Tree is a method to visit all the node in a Binary Tree, In
                                this method left subtree is visited first and then right subtree and lastly root node.
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

left_hot_node = Binary_Tree("Tea")
right_hot_node =Binary_Tree("Coffee")

left_node.add_children(left_hot_node, right_hot_node)

left_cold_node = Binary_Tree("Soda")
right_cold_node = Binary_Tree("Cola")

right_node.add_children(left_cold_node, right_cold_node)


def preOrder_traversal(root_node):
    if not root_node:
        return
    print(root_node.data)
    preOrder_traversal(root_node.left_child)
    preOrder_traversal(root_node.right_child)

def inOrder_traversal(root_node):
    if not root_node:
        return
    inOrder_traversal(root_node.left_child)
    print(root_node.data)
    inOrder_traversal(root_node.right_child)

def postOrder_traversal(root_node):
    if not root_node:
        return
    postOrder_traversal(root_node.left_child)
    postOrder_traversal(root_node.right_child)
    print(root_node.data)


if __name__ == "__main__":
    print(__doc__)
    print("PreOrder Traversal")
    preOrder_traversal(root_node)
    print("\nInOrder Traversal")
    inOrder_traversal(root_node)
    print("\nPostOrder Traversal")
    postOrder_traversal(root_node)