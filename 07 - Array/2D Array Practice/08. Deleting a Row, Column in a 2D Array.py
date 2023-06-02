import numpy as np

class Two_D_Array:
    '''
    Deleting Row/Column into a 2D array
    axis = 0 -> Row
    axis = 1 -> Column
    '''

    def append_into_2D_array(self):
        twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])
        newTwoDArray_row = np.delete(twoDArray, 1, axis=0) # Deleting rows
        newTwoDArray_column = np.delete(twoDArray, 1, axis=1) # Deleting column
        print(newTwoDArray_row,"\n")
        return newTwoDArray_column


if __name__ == "__main__":
    print(Two_D_Array().__doc__)
    print(Two_D_Array().append_into_2D_array())