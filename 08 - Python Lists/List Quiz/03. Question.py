class Lists:
    '''
    What will be the output of the following code snippet?

    A. Syntax error
    B. [4, 3, 2]
    C. [4, 3]
    D. [4, 3, 2, 1]
    '''

    def slicing(self):
        a = [1, 2, 3, 4, 5]
        print(a[3:0:-1])

if __name__ == "__main__":
    print(Lists().__doc__)
    # Lists().slicing()