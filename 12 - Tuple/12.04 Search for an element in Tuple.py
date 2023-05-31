class Tuple:
    '''
    Search
    In Operator
    Time - O(n)
    Space - O(1)
    Linear search - Time O(n), space O(1)
    index - Time O(n), space O(1)
    '''

    def in_operator_tuple(self):
        newTuple = ('a', 'b', 'c', 'd', 'e')
        print('a' in newTuple)

    def search_in_tuple(self, pTuple, element):
        for i in pTuple:
            if i == element:
                return pTuple.index(i)
        return 'The element does not exist'

newTuple = ('a', 'b', 'c', 'd', 'e')

if __name__ == "__main__":
    print(Tuple().__doc__)
    Tuple().in_operator_tuple()
    print(Tuple().search_in_tuple(newTuple, 'a'))