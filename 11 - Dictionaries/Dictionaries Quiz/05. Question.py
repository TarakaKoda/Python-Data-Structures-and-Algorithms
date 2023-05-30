class Dictionary:
    '''
    What will be the output of the following code snippet?

    A. 7
    B. Syntax error
    C. 3
    D. 6
    '''

    def sum_dict(self):
        my_dict = {}
        my_dict[1] = 1
        my_dict['1'] = 2
        my_dict[1.0] = 4

        sum = 0
        for k in my_dict:
            sum += my_dict[k]
        return sum

if __name__ == "__main__":
    print(Dictionary().__doc__)
    # print(Dictionary().sum_dict())