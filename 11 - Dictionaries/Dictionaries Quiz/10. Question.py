class Dictionary:
    '''
    What will be the output of the following code snippet?

    A. True
    B. False
    C. 1
    D. Exception
    '''

    def copy_dict(self):
        rec = {"Name": "Python", "Age": "20", "Addr": "NJ", "Country": "USA"}
        id1 = id(rec)
        del rec
        rec = {"Name": "Python", "Age": "20", "Addr": "NJ", "Country": "USA"}
        id2 = id(rec)
        print(id1 == id2)


if __name__ == "__main__":
    print(Dictionary().__doc__)
    # Dictionary().copy_dict()