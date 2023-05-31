class Tuple:
    '''
    What will be the output of the following code block?

    A. 0
    B.  1
    C. False
    D. True
    '''

    def check_tuple(self):
        init_tuple_a = 'a', 'b'
        init_tuple_b = ('a', 'b')

        print(init_tuple_a == init_tuple_b)

if __name__ == "__main__":
    print(Tuple().__doc__)
    # Tuple().check_tuple()