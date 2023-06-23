class Selection:
    @staticmethod
    def sort(array, reverse=False):
        if len(array) == 1:
            return array
        elif not reverse:
            for i in range(len(array)):
                minimum_value = i
                for j in range(i+1, len(array)):
                    if array[minimum_value] > array[j]:
                        minimum_value = j
                array[i] , array[minimum_value] = array[minimum_value], array[i]
        else:
            for i in range(len(array)):
                minimum_value = 1
                for j in range(i+1, len(array)):
                    if array[minimum_value] < array[j]:
                        minimum_value = j
                array[i],  array[minimum_value], = array[minimum_value], array[i]
        return array

numbers = [2,3,1,4,6,5,7,9,8]

if __name__ == "__main__":
    print(Selection.sort(numbers, True))
