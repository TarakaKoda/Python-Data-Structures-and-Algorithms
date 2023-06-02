import numpy as np

class Two_D_Array:
    '''
    Searching a given element in a 2D Array
    '''

    def searching_element(self, array, value):
        if len(array) and len(array[0]) == 1:
            return array[0][0]
        else:
            for i in range(len(array)):
                for j in range(len(array[0])):
                    if array[i][j] == value:
                        return f"{value} found at {i},{j}"
            return f"Element of not found"

twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])

if __name__ =="__main__":
    print(Two_D_Array().__doc__)
    print(Two_D_Array().searching_element(twoDArray, 9))