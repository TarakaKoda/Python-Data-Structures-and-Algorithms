class Binary_Tree:
    def __init__(self, size):
        self.list = size  * [None]
        self.last_used_index = 0
        self.maximum_size = size

    def insert(self, value):
        if self.last_used_index+1 == self.maximum_size:
            return "Tree is full"
        else:
            self.list[self.last_used_index+1] = value
            self.last_used_index += 1
            return "Successfully inserted"

    def __str__(self):
        values = [str(value) for value in self.list]
        return "\n".join(values)

binary_tree = Binary_Tree(5)

binary_tree.insert("Drinks")
binary_tree.insert("Hot")
binary_tree.insert("Cold")
binary_tree.insert("Tea")

if __name__ == "__main__":
    print(binary_tree)