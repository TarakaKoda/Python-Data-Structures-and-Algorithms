import numpy as np

class Two_D_Array:
    '''
    Traversing through a 2D Array
    '''

    def traversing(self, array):
        for i in range(len(array)):
            for j in range(len(array[0])):
                print(array[i][j])

twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])


if __name__ == "__main__":
    print(Two_D_Array().__doc__)
    Two_D_Array().traversing(twoDArray)