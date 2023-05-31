class Tuple:
    '''
    What will be the output of the following code block?

    A. Nothing gets printed.
    B.  4
    C. 10
    D. TypeError: unsupported operand type
    '''

    def sum_tuple(self):
        init_tuple_a = 1, 2
        init_tuple_b = (3, 4)

        [print(sum(x)) for x in [init_tuple_a + init_tuple_b]]


if __name__ == "__main__":
    print(Tuple().__doc__)
    # Tuple().sum_tuple()