class AVL_Tree:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.height = 1          # to check if the tree is balance or not

new_avl_tree = AVL_Tree(10)

if __name__ == "__main__":
    print(new_avl_tree.data)