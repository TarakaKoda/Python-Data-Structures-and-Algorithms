class Selection:

    @staticmethod
    def sort(array, reverse=False):
        if array is None:
            return None
        if len(array) == 1:
            return array
        elif not reverse:
            for i in range(len(array)):
                minimum_index = i
                for j in range(i+1, len(array)):
                    if array[minimum_index] > array[j]:
                        minimum_index = j
                array[i], array[minimum_index] = array[minimum_index], array[i]
        else:
            for i in range(len(array)):
                minimum_number = i
                for j in range(i+1, len(array)):
                    if array[minimum_number] < array[j]:
                        minimum_number = j
                array[i], array[minimum_number] = array[minimum_number], array[i]
        return array

numbers = [4,5,7,3,2,6,1]

if __name__ == "__main__":
    print(Selection().sort(numbers))
    print(Selection().sort(numbers, True))