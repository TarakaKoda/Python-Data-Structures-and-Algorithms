class Dictionary:
    '''
    Creating a Dictionary
    '''

    def create_dictionary(self):
        my_dict ={"name": "john", "age": 24, "address": "vizag", "eduction": "masters"}
        return my_dict

if __name__ == "__main__":
    print(Dictionary().__doc__)
    print(Dictionary().create_dictionary())
