class Tuple:
    '''
    Tuples in Memory
    Like arrays and list tuples are adjusted side by side in the memory location.
    Accessing Tuples
    tuple[index].tuple[start:end:step]
    Time - O(1)
    space - O(1)
    '''
    def accessing_tuple(self):
        '''Access Tuple elements'''

        newTuple = ('a', 'b', 'c', 'd', 'e')
        print(newTuple[0])


if __name__ == "__main__":
    print(Tuple().__doc__)
    Tuple().accessing_tuple()