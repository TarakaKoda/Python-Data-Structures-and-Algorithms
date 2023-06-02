class Dictionary:
    '''
    Traverse through a dictionary
    '''

    def traverse_dict(self, dict):
        for key in dict:
            print(key, dict[key])

my_dict ={"name": "john", "age": 24, "address": "vizag", "eduction": "masters"}

if __name__ == "__main__":
    print(Dictionary().__doc__)
    Dictionary().traverse_dict(my_dict)