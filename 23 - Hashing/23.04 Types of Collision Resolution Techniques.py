class Hashing:
    '''
    Collision resolution techniques
    - Direct Chaining
    - Open Addressing
       - Linear Probing
       - Quadratic Probing
       - Double hashing

    - Direct Chaining - implements the buckets as linked list. Colliding elements are sorted in lists
    - Open addressing - colliding elements are stored in other vacant buckets. During storage and lookup these are found through so called probing
    - Linear probing - It pleases new key into the closest following empty cell
    - Quadratic probing - Adding arbitrary quadratic polynomial to the index until an empty cell is found
    - Double hashing - Interval between problems is computed by another hash function
    '''

if __name__ == "__main__":
    print(Hashing().__doc__)