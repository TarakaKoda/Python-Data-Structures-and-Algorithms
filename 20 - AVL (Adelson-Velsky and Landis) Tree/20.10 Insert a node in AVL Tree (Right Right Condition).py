class AVL_Tree:
    '''
    right-right Condition: If the balance factor(height difference of the left and right subtrees) of a node is greater than 1 and the new node is inserted into the right subtree
                         of the right child of that node, perform a left rotation to restore balance.
    '''

# For right right Condition: Left Rotation is required

# Algorithm for Left Rotation:
def left_rotation(disbalanced_node):
    new_root = disbalanced_node.right_child
    disbalanced_node.right_child = disbalanced_node.right_child.left_child
    new_root.left = disbalanced_node
    # Update height of disbalanced node and new root
    return new_root

# If we inserted a new node to right child of the right child of root node and the AVL Tree, and it becomes imbalanced
# we use right right CONDITION

if __name__ == "__main__":
    print(AVL_Tree().__doc__)
