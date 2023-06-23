class Bubble:

    @staticmethod
    def sort(array, reverse=False):
        if not array:
            return None
        if len(array) == 1:
            return array
        elif not reverse:
            for i in range(len(array)):
                for j in range(len(array)-i-1):
                    if array[j] > array[j + 1]:
                        array[j], array[j + 1] = array[j + 1], array[j]

        else:
            for i in range(len(array)):
                for j in range(len(array)-i-1):
                    if array[j] < array[j + 1]:
                        array[j], array[j + 1] = array[j + 1], array[j]
        return array

    @staticmethod
    def optimized(array, reverse=False):
        if array is None:
            return None
        if len(array) == 1:
            return array
        swap = False
        if reverse is False:
            for i in range(len(array)):
                for j in range(len(array)-i-1):
                    if array[j] > array[j + 1]:
                        array[j], array[j + 1] = array[j + 1], array[j]
                        swap = True
                if not swap:
                    break
        else:
            for i in range(len(array)):
                for j in range(len(array)-i-1):
                    if array[j] < array[j+1]:
                        array[j], array[j+1] = array[j+1], array[j]
                        swap = True
                if not swap:
                    break
        return array
    @staticmethod
    def recursive(array, n=None):
        if n == None:
            n = len(array)
        if n == 1:
            return array
        swap = False
        for i in range(n-1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] =  array[i + 1], array[i]
                swap = True
        if swap is None:
            return
        Bubble.recursive(array, n-1)


numbers = [9,5,6,4,3,2,8,1,7]

if __name__ == "__main__":
    print(Bubble.sort(numbers, True))
    print(Bubble.optimized(numbers, True))
    Bubble.recursive(numbers)
    print(numbers)
