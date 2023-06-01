class Project:
    '''
Write a function to calculate the average temperature and count the number of days above average.
    '''

    def calculating_temperature(self):
        num = int(input("How many day's temperature? "))
        my_list = []
        for i in range(1, num + 1):
            temp = int(input(f"Enter the maximum temperature of Day {i}: "))
            my_list.append(temp)
        average = round(sum(my_list) / num, 2)
        above_average = 0
        for i in my_list:
            if i > average:
                above_average += 1
        return f"Average: {average}\n{above_average} day(s) are above average temperature"


if __name__ == "__main__":
    print(Project().__doc__)
    print(Project().calculating_temperature())