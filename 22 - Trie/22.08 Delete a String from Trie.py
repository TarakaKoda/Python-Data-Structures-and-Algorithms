class Trie_Node:
    def __init__(self):
        self.children = {}
        self.end_of_string = False

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
        current.end_of_string = True

    def search(self, word):
        current = self.root_node
        for i in word:
            ch = i
            node = current.children.get(ch)
            if node == None:
                return False
            current = node
        if current.end_of_string == False:
            return False
        else:
            return True


def delete(root_node, word, index):
    ch = word[index]
    current_node = root_node.children.get(ch)
    can_this_be_deleted = False

    if len(current_node.children) > 1:
        delete(current_node, word, index+1)
        return False

    if index == len(word)-1:
        if len(current_node.children) >= 1:
            current_node.end_of_string = False
            return False
        else:
            root_node.children.pop(ch)
            return True

    if current_node.end_of_string == True:
        delete(current_node, word, index+1)
        return False

    can_this_be_deleted = delete(current_node, word, index+1)
    if can_this_be_deleted == True:
        root_node.children.pop(ch)
        return True
    else:
        return False


new_trie = Trie()

if __name__ == "__main__":
    new_trie.insert("apple")
    new_trie.insert("appart")
    print(new_trie.search("apple"))
    delete(new_trie.root_node, "appart", 0)
    print(new_trie.search("appart"))
