class Binary_Search_Tree:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


binary_search_tree = Binary_Search_Tree(25)

if __name__ == "__main__":
    print(binary_search_tree.data)