class List:
    '''
    Creating a simple List
    '''

    def create_list(self):
        my_list = [1, 2 , 3, 4, 5, 6]
        return my_list


if __name__ == "__main__":
    print(List().__doc__)
    print(List().create_list())