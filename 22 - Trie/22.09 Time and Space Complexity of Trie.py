class Trie:
    '''
    --------------------------------------------------------------------------------------------------------
        Operation                              Time Complexity                         Space Complexity
    --------------------------------------------------------------------------------------------------------
    Insertion                                      O(L)                                     O(L)
    Search                                         O(L)                                     O(1)
    Deletion                                       O(L)                                     O(1)
    Traversal                                      O(N*M)                                   O(N*M)

    Note:
        L: Length of the word being inserted, searched, or deleted.
        N: Number of words inserted into the trie.
        M: Average length of the words inserted into the trie.
    '''


if __name__ == "__main__":
    print(Trie().__doc__)