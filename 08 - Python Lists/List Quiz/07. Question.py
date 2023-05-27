class Lists:
    '''
    What will be the output of the following code snippet?

    A. 1 2 3 4
    B. 1 4 8 12
    C. 4 7 11 15
    D. 12,13,14,15
    '''
    def array(self):
        arr = [[1, 2, 3, 4],
               [4, 5, 6, 7],
               [8, 9, 10, 11],
               [12, 13, 14, 15]]
        for i in range(0, 4):
            print(arr[i].pop())

if __name__ == "__main__":
    print(Lists().__doc__)
    # Lists().array()
