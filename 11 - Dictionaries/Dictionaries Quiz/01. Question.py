class Dictionary:
    '''
    What will be the output of the following code snippet?
    
    A. Key Error
    B.  1
    C. {(2,3):2}
    D. {(1,2):1}
    '''

    def key_values(self, dict):
        return dict[1,2]

a = {(1,2):1,(2,3):2}

if __name__ == "__main__":
    print(Dictionary().__doc__)
    # print(Dictionary().key_values(a))