class Lists:
    '''
    What will be the output of the following code snippet?

    A. 1 2 3 4 5 6
    B. 2 3 4 5 6 1
    C. 1 1 2 3 4 5
    D. 2 3 4 5 6 6
    '''
    def looping(self, arr):
        for i in range(1, 6):
            arr[i - 1] = arr[i]
        for i in range(0, 6):
            print(arr[i], end=" ")

arr = [1, 2, 3, 4, 5, 6]

if __name__ == "__main__":
    print(Lists().__doc__)
    # Lists().looping(arr)