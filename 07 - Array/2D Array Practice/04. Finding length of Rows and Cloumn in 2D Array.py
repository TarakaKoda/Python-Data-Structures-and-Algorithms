import numpy as np

class Two_D_Array:
    '''
    Finding the length of Rows/Column in 2D Array
    Number of Rows = len(array)
    Number of Columns = len(array[0])
    '''

    def finding_length_of_row_column(self):
        twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])
        print(twoDArray, "\n")
        print(f"Length of Rows: {len(twoDArray)}")
        return f"Length of Columns: {len(twoDArray[0])}"


if __name__ == "__main__":
    print(Two_D_Array().__doc__)
    print(Two_D_Array().finding_length_of_row_column())