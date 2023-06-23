class Merge:

    @staticmethod
    def merge(left, right):
        result = []
        i , j = 0, 0
        while i< len(left) and j < len(right):
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

numbers = [2,3,-1, 5, -1,1,3,5,9, 6, 4,8,1,7]


if __name__ == "__main__":
    print(Merge.merge_sort(numbers))
