class Binary_Tree:
    def __init__(self, size):
        self.list = size * [None]
        self.last_used_index = 0
        self.maximum_size = size

    def insert(self, value):
        if self.last_used_index+1 == self.maximum_size:
            return "Binary Tree is full"
        else:
            self.list[self.last_used_index+1] = value
            self.last_used_index += 1
            return "Successfully inserted"

    def search(self, value):
        if self.last_used_index == 0:
            return "Binary Tree is empty"
        else:
            for i in range(len(self.list)):
                if self.list[i] == value:
                    return "Found"
        return "Value is not present in Binary Tree"

    def preOrder_traversal(self, index):
        if index > self.last_used_index:
            return
        else:
            print(self.list[index])
            self.preOrder_traversal(index*2)
            self.preOrder_traversal(index*2+1)

    def inOrder_traversal(self, index):
        if index > self.last_used_index:
            return
        else:
            self.inOrder_traversal(index * 2)
            print(self.list[index])
            self.inOrder_traversal(index * 2 + 1)

    def postOrder_traversal(self, index):
        if index > self.last_used_index:
            return
        else:
            self.postOrder_traversal(index * 2)
            self.postOrder_traversal(index * 2 + 1)
            print(self.list[index])

    def levelOrder_traversal(self, index):
        if index > self.last_used_index:
            return
        else:
            for i in range(index, self.last_used_index+1):
                print(self.list[i])

    def delete_node(self, value):
        if self.last_used_index == 0:
            return "There is not node to delete in binary tree"
        for i in range(self.last_used_index+1):
            if self.list[i] == value:
                self.list[i] = self.list[self.last_used_index]
                self.list[self.last_used_index] = None
                self.last_used_index -= 1
                return "The node has been successfully deleted"


binary_tree = Binary_Tree(8)
binary_tree.insert("Drinks")
binary_tree.insert("Hot")
binary_tree.insert("Cold")
binary_tree.insert("Tea")
binary_tree.insert("Coffee")
binary_tree.insert("Soda")
binary_tree.insert("Cola")


if __name__ == "__main__":
    print(binary_tree.delete_node("Tea"))
    binary_tree.levelOrder_traversal(1)