class AVL_Tree:
    '''
    Left-Right Condition: If the balance factor(height difference of the left and right subtrees) of a node is greater than 1 and the new node is inserted into the left subtree
                         of the right child of that node, perform a left rotation and then right rotation to restore balance.
    '''

# For Left-Right Condition: Left Rotation and then Right Rotation

# Step 1: rotate left disbalanced node LEFT CHILD
# step 2: rotate right disbalanced node

# Algorithm for left rotation:
def left_rotation(disbalanced_node):  # note: In the case of left rotation we perform rotation to the disbalanced node left child
    new_root = disbalanced_node.right_child
    disbalanced_node.right_child = disbalanced_node.right_child.left_child
    new_root.left_child = disbalanced_node
    # Update height of disbalanced node and new root
    return new_root

# Algorithm for right rotation
def right_rotation(disbalanced_node):
    new_root = disbalanced_node.left_child
    disbalanced_node.left_child = disbalanced_node.left_child.right_child
    new_root.right = disbalanced_node
    # Update height of disbalanced node and new root
    return new_root



if __name__ == "__main__":
    print(AVL_Tree().__doc__)
