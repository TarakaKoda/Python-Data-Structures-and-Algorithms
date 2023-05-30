class Dictionary:
    '''
    What will be the output of the following code snippet?

    A. Key Error
    B. [1,2]
    C. {‘a’:1,’b’:2}
    D. (1,2)
    '''

    def Key_values(self, dict):
        return dict["a", "b"]


a = {'a':1,'b':2,'c':3}

if __name__ == "__main__":
    print(Dictionary().__doc__)
    # print(Dictionary().Key_values(a))