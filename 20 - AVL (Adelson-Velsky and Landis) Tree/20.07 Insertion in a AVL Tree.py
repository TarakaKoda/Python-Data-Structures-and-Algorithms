class AVL_Tree:
    '''
    Insertion in an AVL tree involves adding a new node to the tree while maintaining the balance property of the AVL tree.

    How do we know if rotation is required or not?
    As the definition of the AVL Tree:
    - It is a self-balanced Binary Search Tree, Where the height os left subtree and right subtree is not more than one.

    - The rotation is required when the tree is dis-balanced i.e., The height of left subtree and right subtree differ more than one

    For inserting a node to a AVL Tree we have two cases:
    1. Rotation is not required
    2. Rotation is required

    CASE 1: Rotation is not required
            - In this case the rotation is not required so can preform the same method of insertion as a Binary Search Tree

    CASE 2: Rotation is required
            - we have 4 conditions:
                1. Left Left Condition
                2. Left Right Condition
                3. Right Right Condition
                4. Right Left Condition
    '''


if __name__ == "__main__":
    print(AVL_Tree().__doc__)
