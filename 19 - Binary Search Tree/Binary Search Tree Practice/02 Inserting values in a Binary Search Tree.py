class Binary_Search_Tree:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

def insert(root_node, value):
    if root_node.data == None:
        root_node.data = value
    else:
        if value <= root_node.data:
            if root_node.left_child is None:
                root_node.left_child = Binary_Search_Tree(value)
            else:
                insert(root_node.left_child, value)
        else:
            if root_node.right_child is None:
                root_node.right_child = Binary_Search_Tree(value)
            else:
                insert(root_node.right_child, value)
    return "value Successfully inserted"

binary_search_tree = Binary_Search_Tree(80)

if __name__ == "__main__":
    print(insert(binary_search_tree,50))
    print(insert(binary_search_tree,60))
    print(binary_search_tree.data)
    print(binary_search_tree.left_child.data)