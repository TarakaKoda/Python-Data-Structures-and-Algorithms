class Lists:
    '''
    What will be the output of the following code snippet?

    A. [1] [2] [3]
    B. [1, 2, 3]
    C. [1] [1, 2] [1, 2, 3]
    D. 1 2 3
    '''

    def f(self,i, values = []):
        values.append(i)
        print (values)
        return values

if __name__ == "__main__":
    print(Lists().__doc__)
    # Lists().f(1)
    # Lists().f(2)
    # Lists().f(3)
