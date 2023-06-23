class Merge:
    '''
     Merge Sort
      - It is a divide and conquer algorithm
      - Divide the input array in two halves, and we keep having recursively until they become too small that cannot be broken further
      - merge halves by sorting them
      Time O(N logN) space O(n)
      merge sort is out place algorithm
      merge sort is stable
      when to use merge sort?
      - when you need stable sort
      - when average expected time in O(N logN)
      when to avoid stable sort?
      - when space is a concern
    '''

    @staticmethod
    def merge(left, right):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        return result

    @staticmethod
    def merge_sort(array):
        if len(array) <= 1:
            return array
        mid = int(len(array)/2)
        left = Merge.merge_sort(array[:mid])
        right = Merge.merge_sort(array[mid:])
        return Merge.merge(left, right)


numbers = [8, 1, 6, 2, 7, 4]

if __name__ == "__main__":
    print(Merge.merge_sort(numbers))
