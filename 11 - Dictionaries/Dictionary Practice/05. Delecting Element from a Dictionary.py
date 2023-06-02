class Dictionary:
    '''
    Deleting or remove element from a dictionary
    '''

    def delecting_element(self, dict):
        print(f"Original Dictionary: {dict}")
        print(f'After pop(): {dict.pop("name")}')
        print(f"After popitem(): {dict.popitem()}")
        # dict.clear()
        # del dict
        return f"Original Dictionary after deleting elements: {dict}"

my_dict ={"name": "john", "age": 24, "address": "vizag", "eduction": "masters"}


if __name__ == "__main__":
    print(Dictionary().__doc__)
    print(Dictionary().delecting_element(my_dict))