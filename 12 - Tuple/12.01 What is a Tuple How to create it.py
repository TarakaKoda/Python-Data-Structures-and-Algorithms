class Tuple:
    '''
    What is Tuple
    A tuple is an immutable sequence of python objects
    Tuples are also comparable and hashable
    Time - O(1)
    Space - O(n)
    '''

    def crate_tuple(self):
        '''How to create a Tuple?'''
        newTuple = ('a', 'b', 'c', 'd', 'e')
        newTuple1 = tuple('abcde')

        print(newTuple1)


if __name__ == "__main__":
    print(Tuple().__doc__)
    Tuple().crate_tuple()