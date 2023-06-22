class Insertion:
    '''
    Insertion sort
      - Divide the given array into two parts
      - Take first element from unsorted array and fund its correct position in sorted array
      - Repeat until unsorted array is empty

    Time O(n^2) Space O(1)
      It is in place and stable algorithm

    when to use insertion sort?
      - when we have insufficient memory
      - Easy to implement
      - when we have contiguous inflow of numbers, and we want to keep them sorted

    when to avoid insertion sort
      - when time is a concern
    '''
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
    print(Insertion.__doc__)
    print(Insertion.Sort(numbers, True))
