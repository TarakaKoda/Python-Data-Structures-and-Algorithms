class List:
    '''
    Searching for an element in the List
    '''

    def searching_element(self, list, value):
            for i in range(len(list)):
                if list[i] == value:
                    return f"{value} found at index {i}"
            return f"{value} does not exist"

my_list = [1,2,3,4,5,6]

if __name__ == "__main__":
    print(List().__doc__)
    print(List().searching_element(my_list, 4))