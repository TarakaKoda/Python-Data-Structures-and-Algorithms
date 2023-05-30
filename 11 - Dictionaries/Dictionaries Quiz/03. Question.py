class Dictionary:
    '''
    What will be the output of the following code block?

    A. 1
    B. 2
    C. 3
    D. 4
    '''
    def __init__(self):
        self.fruit = {}

    def addone(self, index):
        if index in self.fruit:
            self.fruit[index] += 1
        else:
            self.fruit[index] = 1


if __name__ == "__main__":
    print(Dictionary().__doc__)
    Dictionary().addone('Apple')
    Dictionary().addone('Banana')
    Dictionary().addone('apple')
    # print(len(Dictionary().fruit))
