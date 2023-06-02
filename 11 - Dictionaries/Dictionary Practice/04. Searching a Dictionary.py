class Dictionary:
    '''
    Searching a dictionary
    '''

    def search_dict(self, dict, value):
        for key in dict:
            if dict[key] == value:
                return key, value
        return 'The value does not exist'

my_dict ={"name": "john", "age": 24, "address": "vizag", "eduction": "masters"}


if __name__ == "__main__":
    print(Dictionary().__doc__)
    print(Dictionary().search_dict(my_dict, "vizag"))