class Bubble:

    @staticmethod
    def sort(array, reverse=False):
        if not reverse:
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
        if reverse:
            swap = False
            for i in range(len(array) - 1):
                for j in range(len(array) - i - 1):
                    if array[j] < array[j + 1]:
                        array[j], array[j + 1] = array[j + 1], array[j]
                        swap = True
                if not swap:
                    break
        else:
            swap = False
            for i in range(len(array) - 1):
                for j in range(len(array) - i - 1):
                    if array[j] > array[j + 1]:
                        array[j], array[j + 1] = array[j + 1], array[j]
                        swap = True
                if not swap:
                    break
        return array

    @staticmethod
    def recursive(array, n=None):
        if not n:
            n = len(array)
        if n == 1: return
        swap = False
        for i in range(n-1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swap = True
        if not swap:
            return
        Bubble.recursive(array, n-1)


numbers = [2,3,4,5,6,1,7,8]

if __name__ == "__main__":
    print(Bubble.sort(numbers, False))
    Bubble.recursive(numbers)
    print(numbers)