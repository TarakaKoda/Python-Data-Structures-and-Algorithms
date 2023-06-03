class Tuple:
    '''
    How to create a Tuple
    '''

    def create_tuple(self):
        newTuple = ('a', 'b', 'c', 'd', 'e')
        newTuple1 = tuple('abcde')
        print(newTuple)
        return newTuple1


if __name__ == "__main__":
    print(Tuple().__doc__)
    print(Tuple().create_tuple())

