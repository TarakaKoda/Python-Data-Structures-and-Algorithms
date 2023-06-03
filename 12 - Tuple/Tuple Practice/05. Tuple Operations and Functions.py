class Tuple:
    '''
    Tuple Operations / Functions
    '''

    def tuple_operations(self, myTuple, myTuple1):
        print(myTuple + myTuple1)
        print(myTuple * 4)
        print(2 in myTuple1)

        print(myTuple1.count(2))
        return myTuple1.index(2)

myTuple = (1,4,3,2,5)
myTuple1 = (1,2,6,9,8,7)

if __name__ == "__main__":
    print(Tuple().__doc__)
    print(Tuple().tuple_operations(myTuple, myTuple1))