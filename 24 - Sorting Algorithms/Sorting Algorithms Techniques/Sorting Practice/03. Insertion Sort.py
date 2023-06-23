class Insertion:
    @staticmethod
    def sort(array, reverse=False):
        if len(array) == 1:
            return array
        elif not reverse:
            for i in range(1, len(array)):
                key = array[i]
                j = i-1
                while j>=0 and key < array[j]:
                    array[j+1] = array[j]
                    j -= 1
                array[j+1] = key
        else:
            for i in range(1, len(array)):
                key = array[i]
                j = i -1
                while j>=0 and key > array[j]:
                    array[j+1] = array[j]
                    j -=1
                array[j+1] = key
        return array
numbers = [2,5,1,3,6,4,7,9,8]

if __name__ == "__main__":
    print(Insertion.sort(numbers, True))