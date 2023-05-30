class Dictionary:
    '''
    What will be the output of the following code snippet?

    A. True
    B. False
    C. 0
    D. 1
    '''

    def copy_dict(self, rec):
        r = rec.copy()
        print(id(r) == id(rec))


rec = {"Name" : "Python", "Age":"20"}

if __name__ == "__main__":
    print(Dictionary().__doc__)
    # Dictionary().copy_dict(rec)