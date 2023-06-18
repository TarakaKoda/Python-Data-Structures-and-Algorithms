class AVL_Tree:
    '''
    Right-Left Condition: If the balance factor(height difference of the left and right subtrees) of a node is greater than 1 and the new node is inserted into the right subtree
                         of the left child of that node, perform a right rotation and then left rotation to restore balance.
    '''

# For Right-Left Condition: Right Rotation and then Left Rotation

# Step 1: rotate right disbalanced node RIGHT CHILD
# step 2: rotate left disbalanced node

# Algorithm for Right Rotation:
def right_rotation(disbalanced_node):  # note: In the case of right rotation we perform rotation to the disbalanced node right child
    new_root = disbalanced_node.left_child
    disbalanced_node.left_child = disbalanced_node.left_child.right_child
    new_root.right = disbalanced_node
    # Update height of disbalanced node and new root
    return new_root

# Algorithm for left rotation:
def left_rotation(disbalanced_node):
    new_root = disbalanced_node.right_child
    disbalanced_node.right_child = disbalanced_node.right_child.left_child
    new_root.left_child = disbalanced_node
    # Update height of disbalanced node and new root
    return new_root


if __name__ == "__main__":
    print(AVL_Tree().__doc__)
