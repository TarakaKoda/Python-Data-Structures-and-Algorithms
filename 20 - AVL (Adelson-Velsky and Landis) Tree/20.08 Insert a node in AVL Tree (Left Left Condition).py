class AVL_Tree:
    '''
    Left-Left Condition: If the balance factor(height difference of the left and right subtrees) of a node is greater than 1 and the new node is inserted into the left subtree
                         of the left child of that node, perform a right rotation to restore balance.
    '''

# For Left Left Condition: Right Rotation is required

# Algorithm for Right Rotation:
def right_rotation(disbalanced_node):
    new_root = disbalanced_node.left_child
    disbalanced_node.left_child = disbalanced_node.left_child.right_child
    new_root.right = disbalanced_node
    # Update height of disbalanced node and new root
    return new_root

# If we inserted a new node to left child of the left child of root node and the AVL Tree, and it becomes imbalanced
# we use LEFT LEFT CONDITION

if __name__ == "__main__":
    print(AVL_Tree().__doc__)
