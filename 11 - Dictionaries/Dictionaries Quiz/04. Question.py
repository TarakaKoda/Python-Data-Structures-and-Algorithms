class Dictionary:
    '''
    What will be the output of the following code block?

    A. 1
    B. 2
    C. 3
    D. 4
    '''

    def sum_dict(self):
        arr = {}
        arr[1] = 1
        arr['1'] = 2
        arr[1] += 1

        sum = 0
        for k in arr:
            sum += arr[k]
        return sum

if __name__ == "__main__":
    print(Dictionary().__doc__)
    # print(Dictionary().sum_dict())