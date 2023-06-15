class Binary_Tree:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def add_children(self, left_child, right_child):
        self.left_child = left_child
        self.right_child = right_child


root_node = Binary_Tree("Drinks")
left_node = Binary_Tree("Hot")
right_node = Binary_Tree("Cold")

root_node.add_children(left_node, right_node)

left_hot_node = Binary_Tree("Tea")
right_hot_node = Binary_Tree("Coffee")

left_node.add_children(left_hot_node, right_hot_node)

left_cold_node = Binary_Tree("Soda")
right_cold_node = Binary_Tree("Cola")

right_node.add_children(left_cold_node, right_cold_node)

