class Tuple:
    '''
    Traversing through a Tuple
    '''

    def traverse_tuple(self, tuple):
        # using range() and len()
        for i in range(len(tuple)):
            print(tuple[i])
        print(" ")
        for i in tuple:
            print(i)

my_tuple = ("a","b","c","d")

if __name__ == "__main__":
    print(Tuple().__doc__)
    Tuple().traverse_tuple(my_tuple)