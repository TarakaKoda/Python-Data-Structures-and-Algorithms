class Hashing:
    '''
    pros and cons of collision resolution techniques
      Direct chaining -
      - Hash table never gets full
      - Higher linked list causes performance leaks(The time complexity of search operation becomes O(n)).
      open addressing
      - Easy implementation
      - when hash table is full, creation of new hash table affects performance (Time complexity for search operation becomes O(n)).

      If input size is known we always use open addressing
      If we perform deletion operation more frequently we use "Direct chaining"
    '''


if __name__ == "__main__":
    print(Hashing().__doc__)