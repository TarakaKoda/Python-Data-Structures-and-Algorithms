class Hashing:
    '''
    What is hashing?
    - Hashing is a method of sorting and indexing data. The idea behind hashing is to allow large amount of data to be
      indexed using keys commonly created by formulas

                    magic function
      Apple                             18
      Airplane                          20
      Animals                           22

    Why Hashing?
    - It is time efficient case of search operation:
        +------------------+---------------------+
        | Data Structure   | Time Complexity     |
        +------------------+---------------------+
        | Array/Python list| O(logN)             |
        +------------------+---------------------+
        | Linked List      | O(n)                |
        +------------------+---------------------+
        | Tree             | O(logN)             |
        +------------------+---------------------+
        | Hashing          | O(1) / O(n)         |
        +------------------+---------------------+
'''



if __name__ == "__main__":
    print(Hashing().__doc__)
