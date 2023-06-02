import numpy as np

class Two_D_Array:
    '''
    Accessing Elements in a 2D Array using indexes: row index, column index
    '''

    def access_elements(self,array, row_index, column_index):
        if len(array) < row_index or len(array[0]) < column_index:
            return "Index out of range"
        else:
            return f"{array}\nindex: ({row_index},{column_index}) = element {array[row_index][column_index]}"

twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])


if __name__ == "__main__":
    print(Two_D_Array().__doc__)
    print(Two_D_Array().access_elements(twoDArray, 3 , 3))