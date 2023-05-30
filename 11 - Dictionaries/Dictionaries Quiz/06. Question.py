class Dictionary:
    '''
    What will be the output of the following code snippet?

    A. Syntax error
    B. 30
        {(1, 2): 12, (4, 2, 1): 10, (1, 2, 4): 8}
    C. 47
        {(1, 2): 12, (4, 2, 1): 10, (1, 2, 4): 8}
    D. 30
        {[1, 2]: 12, [4, 2, 1]: 10, [1, 2, 4]: 8}
    '''

    def sum_dict(self):
        my_dict = {}
        my_dict[(1, 2, 4)] = 8
        my_dict[(4, 2, 1)] = 10
        my_dict[(1, 2)] = 12

        sum = 0
        for k in my_dict:
            sum += my_dict[k]
        return sum

if __name__ == "__main__":
    print(Dictionary().__doc__)
    # print(Dictionary().sum_dict())