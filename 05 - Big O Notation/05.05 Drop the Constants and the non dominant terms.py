class Big_O:
    '''
      Dropping constants and Non-Dominant terms in Big O
      O(2N) -> O(N)
      O(N^2+N) -> O(N^2)
      - It is very possible that O(N) code is frater than O(1) code for specific inputs
      - Different computers with different architectures have different constant factors
      - Different algorithms with the same basic idea and computational complexity might have slightly different constants
      - As n approaches infinity constant factories are not really a big deal
    '''


if __name__ == "__main__":
    print(Big_O().__doc__)