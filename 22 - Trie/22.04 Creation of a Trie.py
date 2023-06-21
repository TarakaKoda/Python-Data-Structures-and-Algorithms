class Trie_Node:
    def __init__(self):
        self.children = {}
        self.end_of_string = False

class Trie:
    def __init__(self):
        self.root_node = Trie_Node()


new_trie = Trie()
