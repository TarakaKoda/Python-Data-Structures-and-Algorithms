class Dictionary:
    '''
    What will be the output of the following code snippet?

    A. 1
    B. 3
    C. 4
    D. Type Error
    '''

    def collections(self):
        box = {}
        jars = {}
        crates = {}
        box['biscuit'] = 1
        box['cake'] = 3
        jars['jam'] = 4
        crates['box'] = box
        crates['jars'] = jars
        return len(crates[box])


if __name__ == "__main__":
    print(Dictionary().__doc__)
    # print(Dictionary().collections())