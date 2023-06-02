class List:
    '''
    List Operations/Functions
    '''

    def calculating_average_without_list_fun(self):
        total = 0
        count = 0
        while (True):
            inp = input('Enter a number: ')
            if inp == 'done': break
            value = float(inp)
            total = total + value
            count = count + 1
        average = round(total / count, 2)
        return f"Average: {average}"

    def calculating_average_with_list_fun(self):
        numlist = list()
        while (True):
            inp = input('Enter a number: ')
            if inp == 'done': break
            value = float(inp)
            numlist.append(value)
        average = round(sum(numlist) / len(numlist), 2)
        return f"Average: {average}"


if __name__ == "__main__":
    print(List().__doc__)
    print(List().calculating_average_without_list_fun())
    print(List().calculating_average_with_list_fun())

