class Binary_Tree:
    def __init__(self, size):
        self.list = size * [None]
        self.last_used_index = 0
        self.maximum_size = size

    def insert(self, value):
        if self.last_used_index+1 == self.maximum_size:
            return "Binary Tree is full"
        else:
            self.list[self.last_used_index +1] = value
            self.last_used_index += 1
            return "successfully inserted"

    def searching(self, value):
        if self.last_used_index == 0:
            return "Binary is full"
        else:
            for i in range(len(self.list)):
                if self.list[i] == value:
                    return "Found"
            return "value does not exist in Binary Tree"

    def preOrder_traversal(self, index):
        if index > self.last_used_index:
            return
        else:
            print(self.list[index])
            self.preOrder_traversal(index*2)
            self.preOrder_traversal(index*2 +1)

    def inOrder_traversal(self, index):
        if index > self.last_used_index:
            return
        else:
            self.inOrder_traversal(index*2)
            print(self.list[index])
            self.inOrder_traversal(index*2 +1)

binary_tree = Binary_Tree(8)
binary_tree.insert("Drinks")
binary_tree.insert("Hot")
binary_tree.insert("Cold")
binary_tree.insert("Tea")
binary_tree.insert("Coffee")
binary_tree.insert("Soda")
binary_tree.insert("Cola")


if __name__ == "__main__":
    binary_tree.inOrder_traversal(1)