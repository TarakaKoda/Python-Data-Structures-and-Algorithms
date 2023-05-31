class Tuple:
    '''
    What will be the output of the following code block?

    A. Exception
    B. 5
    C. 4
    D. None
    '''

    def slicing_tuple(self):
        init_tuple = ((1, 2),) * 7
        print(len(init_tuple[3:8]))


if __name__ == "__main__":
    print(Tuple().__doc__)
    # Tuple().slicing_tuple()