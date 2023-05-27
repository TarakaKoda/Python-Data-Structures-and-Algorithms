class Lists:
    '''
    What will be the output of the following code snippet?

    A. 1
    B. 2
    C. 3
    D. 4
    E. 5
    F. 6
    '''

    def fun(self, m):
        v = m[0][0]

        for row in m:
            for element in row:
                if v < element: v = element

        return v

data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
list = Lists()

if __name__ == "__main__":
    print(Lists().__doc__)
    # print(list.fun(data))
