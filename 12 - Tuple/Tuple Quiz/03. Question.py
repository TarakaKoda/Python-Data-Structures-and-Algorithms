class Tuple:
    '''
    What will be the output of the following code block?

    A. (1, 2, 3, 4)
    B.  (‘1’, ‘2’, ‘3’, ‘4’)
    C. [‘1’, ‘2’, ‘3’, ‘4’]
    D. None
    '''
    def adding_tuple(self):
        init_tuple_a = '1', '2'
        init_tuple_b = ('3', '4')

        print(init_tuple_a + init_tuple_b)


if __name__ == "__main__":
    print(Tuple().__doc__)
    # Tuple().adding_tuple()