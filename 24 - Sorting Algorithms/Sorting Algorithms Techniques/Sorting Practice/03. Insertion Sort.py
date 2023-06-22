class Insertion:

    @staticmethod
    def Sort(array, reverse=False):
        if not reverse:
            for i in range(1, len(array)):
                key = array[i]
                j = i - 1
                while j>= 0 and key < array[j]:
                    array[j+1] = array[j]
                    j -= 1
                array[j+1] = key
        else:
            for i in range(1, len(array)):
                key = array[i]
                j = i - 1
                while j>= 0 and key > array[j]:
                    array[j+1] = array[j]
                    j -= 1
                array[j+1] = key
        return array

numbers = [3,5,6,2,1,8,7,4]

if __name__ == "__main__":
    print(Insertion.Sort(numbers, True))
