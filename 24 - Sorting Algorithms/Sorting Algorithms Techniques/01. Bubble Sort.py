class Bubble:
    '''
     Bubble Sort
      - Bubble sort is also referred as Sinking sort
      -we repeatedly compare each pair of adjacent items and swap them if they are in wrong order
      Time O(N^2) Space O(1)
      When to use bubble sort?
      - when the input is already sorted
      - space is concern
      - easy to implement
      when to avoid bubble sort?
      - Average time complexity is poor

      Is an in place and stable type algorithm
    '''
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


numbers = [3,4,2,5,6,7,1]
sorted_number = [1,2,3,4,5,6,7]

if __name__ == "__main__":
    print(Bubble.__doc__)
    print(Bubble.sort(numbers, False))
    print(Bubble.optimized(sorted_number))
    Bubble.recursive(numbers)
    print(numbers)