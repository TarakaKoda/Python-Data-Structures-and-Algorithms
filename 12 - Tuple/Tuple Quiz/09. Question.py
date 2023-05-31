class Tuple:
    '''
    What will be the output of the following code block?

    A. (1, 1, 1)
    B. (2, 2, 2)
    C. (2, 1, 1)
    D. TypeError: ‘tuple’ object does not support item assignment
    '''

    def check_tuple(self):
        init_tuple = (1,) * 3
        init_tuple[0] = 2
        print(init_tuple)


if __name__ == "__main__":
    print(Tuple().__doc__)
    # Tuple().check_tuple()