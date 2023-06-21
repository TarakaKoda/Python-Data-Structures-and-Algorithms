class Trie_Node:
    def __init__(self):
        self.children = {}
        self.end_of_node = False

class Trie:
    def __init__(self):
        self.root_node = Trie_Node()

    def insert(self, word):
        current = self.root_node
        for i in word:
            ch = i
            node = current.children.get(ch)
            if node == None:
                node = Trie_Node()
                current.children.update({ch:node})
            current = node
        current.end_of_node = True

    def search(self, word):
        current = self.root_node
        for i in word:
            ch = i
            node = current.children.get(ch)
            if node == None:
                return False
            current = node
        if current.end_of_node == False:
            return False
        else:
            return True

new_trie = Trie()

if __name__ == "__main__":
    new_trie.insert("apple")
    new_trie.insert("appart")
    print(new_trie.search("apple"))
    print(new_trie.search("app"))