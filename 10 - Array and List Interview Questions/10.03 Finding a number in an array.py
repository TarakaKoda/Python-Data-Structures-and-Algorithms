import numpy as np
class Interview_question3:
    '''
    How to check if an array contains a number in python?
    '''

    def doesExist(self, lis, n):
        for i in range(len(lis)):
            if lis[i] == n:
                return True

myArray = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

if __name__ == "__main__":
    print(Interview_question3().__doc__)
    print(Interview_question3().doesExist(myArray, 12))