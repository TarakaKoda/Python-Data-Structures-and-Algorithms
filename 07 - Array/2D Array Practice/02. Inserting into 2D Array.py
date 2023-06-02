import numpy as np

class Two_D_Array:
    '''
    Inserting Row/Column into a 2D array
    axis = 0 -> Row
    axis = 1 -> Column
    '''

    def insert_into_2D_array(self):
        twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])
        newTwoDArray_row = np.insert(twoDArray, 1, [[1, 2, 3, 4]], axis=0) # Inserting rows
        newTwoDArray_column = np.insert(twoDArray, 2, [[5, 6, 7, 8]], axis=1) # Inserting column
        print(newTwoDArray_row, "\n")
        return newTwoDArray_column


if __name__ == "__main__":
    print(Two_D_Array().__doc__)
    print(Two_D_Array().insert_into_2D_array())