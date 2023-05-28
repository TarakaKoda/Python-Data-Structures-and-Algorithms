import numpy as np

class Interview_question4:
    '''
    Find max product of integers in an array.
    '''

    def findMaxProduct(self, lis):
        assert len(lis) >= 2, "array must contain at least 2 elements to get max product"
        lis.sort()
        max1 = lis[0] * lis[1]
        max2 = lis[-1] * lis[-2]
        return max(max1, max2)

myArray = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

if __name__ == "__main__":
    print(Interview_question4().__doc__)
    print(Interview_question4().findMaxProduct(myArray))