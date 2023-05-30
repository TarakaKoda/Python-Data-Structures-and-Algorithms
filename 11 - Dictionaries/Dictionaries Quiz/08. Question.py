class Dictionary:
    '''
    What will be the output of the following code block?

    A. 96 98 97
    B. 96 97 98
    C. 98 97 96
    D. NameError
    '''

    def sorted_dict(self, dict):
        for _ in sorted(dict):
            print(dict[_], end=" ")


dict = {'c': 97, 'a': 96, 'b': 98}

if __name__ == "__main__":
    print(Dictionary().__doc__)
    # Dictionary().sorted_dict(dict)