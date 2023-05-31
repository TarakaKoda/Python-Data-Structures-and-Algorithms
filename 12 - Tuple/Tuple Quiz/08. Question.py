class Tuple:
    '''
    What will be the output of the following code block?

    A. <class ‘tuple’>
    B. <class ‘str’>
    C. <class ‘list’>
    D. <class ‘function’>
    '''

    def check_type_tuple(self):
        init_tuple = ('Python') * 3

        print(type(init_tuple))


if __name__ == "__main__":
    print(Tuple().__doc__)
    # Tuple().check_type_tuple()