class Trie_Node:
    def __init__(self):
        self.children = {}
        self.end_of_string = False

class Trie:
    def __init__(self):
        self.root_node = Trie_Node()

    def insertion(self, word):
        current = self.root_node
        for i in word:
            ch = i
            node = current.children.get(ch)
            if node is None:
                node = Trie_Node()
                current.children.update({ch:node})
            current = node
        current.end_of_string = True



new_trie = Trie()

if __name__ == "__main__":
    new_trie.insertion("apple")
    print(new_trie)
