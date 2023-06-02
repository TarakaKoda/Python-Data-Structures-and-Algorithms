import numpy as np

class Two_D_Array:
    '''
    Creating a Two Dimensional Array using numpy
    '''

    def create_2d_array(self):
        twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])
        return twoDArray


if __name__ == "__main__":
    print(Two_D_Array().__doc__)
    print(Two_D_Array().create_2d_array())
