class Dictionary:
    '''
    sorted method
    '''

    def sorting_dict(self):
        myDict = {'eooooa': 1, 'aas': 2, 'aa': 3, 'sseo': 4, 'werwi': 5}

        return sorted(myDict, key=len)


if __name__ == "__main__":
    print(Dictionary().__doc__)
    print(Dictionary().sorting_dict())