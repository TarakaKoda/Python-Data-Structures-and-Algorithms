class Tuple:
    '''
    What will be the output of the following code block?

    A. 3
    B. 6
    C. 9
    D. Nothing gets printed.
    '''
    def sum_tuple(self):
        init_tuple = [(0, 1), (1, 2), (2, 3)]
        result = sum(n for _, n in init_tuple)

        print(result)


if __name__ == "__main__":
    print(Tuple().__doc__)
    # Tuple().sum_tuple()