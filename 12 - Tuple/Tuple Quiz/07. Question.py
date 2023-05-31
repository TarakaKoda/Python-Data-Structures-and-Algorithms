class Tuple:
    '''
    What will be the output of the following code block?

    A. ()
    B. (‘Python’)
    C. (‘Python’, ‘Python’)
    D. Runtime Exception.
    '''

    def tuple_slicing(self):
        l = [1, 2, 3]
        init_tuple = ('Python',) * (l.__len__() - l[::-1][0])

        print(init_tuple)

if __name__ == "__main__":
    print(Tuple().__doc__)
    # Tuple().tuple_slicing()