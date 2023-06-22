class Selection:
    '''
     Selection Sort
      - In case of selection sort we repeatedly find the minimum element and move it to the sorted part of array to make unsorted part sorted
      It is unstable and in place Algorithm
      Time O(N^2) Space O(1)
      we can make it space by moving the elements between min and index to left and placing the min at index

      When to use selection sort?
      - when we have insufficient memory
      - Easy to implement
      when to avoid selection sort?
      - when time is a concern
    '''

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

numbers = [2,3,1,5,6,4,7]

if __name__ == "__main__":
    print(Selection().__doc__)
    print(Selection().sort(numbers))
    print(Selection().sort(numbers, True))