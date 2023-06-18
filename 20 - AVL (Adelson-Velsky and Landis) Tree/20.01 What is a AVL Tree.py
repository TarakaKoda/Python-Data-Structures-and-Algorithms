class AVL_Tree:
    '''
    What is a AVL Tree?
    - An AVL (Adelson-Velsky and Landis) Tree is a self-balancing Binary Search Tree.Where the difference between the heights
      of th left and right subtree must be not more than one all nodes.

                                              6
                                            /   \
                                           3     8
                                          / \   / \
                                         2   4 7   9

    - if at any time heights of left and right subtree differ by more than one, then re-balancing is done to restore
      AVL property, this process is called rotation
    '''


if __name__ == "__main__":
    print(AVL_Tree().__doc__)
