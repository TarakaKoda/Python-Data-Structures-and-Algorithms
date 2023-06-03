class Tuple:
    '''
    Searching for an element in a Tuple
    '''

    def searching_element(self, tuple, element):
        for i in range(len(tuple)):
            if tuple[i] == element:
                return f"{element} found at index: {i}"
        else:
            return f"{element} does not exist"

    def searching_using_in(self, tuple, element):
        if element in tuple:
            return f"{element} found at index: {tuple.index(element)}"
        else:
            return f"{element} does not exist"


my_tuple = ("a","b","c","d")

if __name__ == "__main__":
    print(Tuple().__doc__)
    print(Tuple().searching_element(my_tuple, "a"))
    print(Tuple().searching_using_in(my_tuple, "d"))