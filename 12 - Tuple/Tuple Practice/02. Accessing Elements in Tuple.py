class Tuple:
    '''
    Access Tuple elements
    '''

    def access_element(self, tuple):
        return tuple[1]

my_tuple = ("a","b","c","d")

if __name__ == "__main__":
    print(Tuple().__doc__)
    print(Tuple().access_element(my_tuple))