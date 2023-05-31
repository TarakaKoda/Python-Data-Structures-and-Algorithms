class Tuple:
    '''
    Traversal
    Time - O(n)
    space - O(1)
    '''

    def traverse_elements(self):
        '''Traverse through tuple'''

        newTuple = ('a', 'b', 'c', 'd', 'e')
        for i in newTuple:
            print(i)

        for index in range(len(newTuple)):
            print(newTuple[index])

if __name__ == "__main__":
    print(Tuple().__doc__)
    Tuple().traverse_elements()