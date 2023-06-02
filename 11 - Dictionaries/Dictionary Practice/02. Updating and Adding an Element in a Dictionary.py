class Dictionary:
    '''
    Update / add an element to the dictionary
    '''

    def update_add_element(self, dict):
        dict['address'] = 'London'
        new_dict = {"a":1, "b":2, "c":3}
        dict.update(new_dict)
        return dict



my_dict ={"name": "john", "age": 24, "address": "vizag", "eduction": "masters"}

if __name__ == "__main__":
    print(Dictionary().__doc__)
    print(Dictionary().update_add_element(my_dict))