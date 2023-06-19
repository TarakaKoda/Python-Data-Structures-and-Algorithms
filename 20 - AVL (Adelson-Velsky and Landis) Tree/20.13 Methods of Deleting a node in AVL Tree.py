class AVL_Tree:
    '''
    Delete a node
      case 1: the tree does not exist
      case 2: Rotation is not required (Same as the Binary Search Tree)
              - deleting a leaf node
              - deleting a root node with single child node
              - deleting a root node with two children (using a helper function to find the successor of the root node)
                - successor will be root node's right child's left child
      case 3: Rotation is required
             - Left-Left Condition   (Right Rotation)
             - Left-Right Condition  (Left Rotation and then Right Rotation)
             - Right-Right Condition (Left Rotation)
             - Right-Left Condition  (Right Rotation and then Left Rotation)
      All together Insertion takes O(logn) space and time complexity

    '''

if __name__ == "__main__":
    print(AVL_Tree.__doc__)