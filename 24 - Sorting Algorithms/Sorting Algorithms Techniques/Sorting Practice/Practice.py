class Sorting:

    @staticmethod
    def bubble_sort(array: list[int], reverse=False)-> list[int]:
        if len(array) == 1:
            return array
        swap = False
        if not reverse:
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
                    if array[j] < array[j + 1]:
                        array[j], array[j + 1] = array[j + 1], array[j]
        return array

    @staticmethod
    def selection_sort(array: list[int], reverse=False) -> list[int]:
        n = len(array)
        if n <= 1:
            return array
        if not reverse:
            for i in range(n):
                minimum_number = i
                for j in range(i+1, n):
                    if array[minimum_number] > array[j]:
                        minimum_number = j
                array[i], array[minimum_number] = array[minimum_number], array[i]

        else:
            for i in range(n):
                maximum_number = i
                for j in range(i+1, n):
                    if array[maximum_number] < array[j]:
                        maximum_number = j
                array[i], array[maximum_number] = array[maximum_number], array[i]
        return array

    @staticmethod
    def insertion_sort(array: list[int], reverse=False) -> list[int]:
        if len(array) <=1:
            return array
        if not reverse:
            for i in range(len(array)):
                key = array[i]
                j = i - 1
                while j>=0 and key < array[j]:
                    array[j+1] = array[j]
                    j -= 1
                array[j+1] = key
        else:
            for i in range(len(array)):
                key = array[i]
                j = i - 1
                while j>=0 and key > array[j]:
                    array[j + 1] = array[j]
                    j -= 1
                array[j + 1] = key
        return array

    @staticmethod
    def merge(left: list[int], right: list[int]) -> list[int]:
        result = []
        i, j = 0, 0
        while  i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        return result
    @staticmethod
    def merge_sort(array: list[int]) -> list[int]:
        if len(array) <= 1:
            return array
        else:
            mid = len(array)//2
            left = Sorting.merge_sort(array[:mid])
            right = Sorting.merge_sort(array[mid:])
            return Sorting.merge(left, right)

    @staticmethod
    def quick_sort(array: list[int], reverse=False) -> list[int]:
        if len(array) <= 1:
            return array
        if not reverse:
            pivot = array[len(array)//2]
            left = [x for x in array if x < pivot]
            middle = [x for x in array if x == pivot]
            right = [x for x in array if x > pivot]
            return Sorting.quick_sort(left) + middle + Sorting.quick_sort(right)
        else:
            pivot = array[len(array)//2]
            left = [x for x in array if x > pivot]
            middle = [x for x in array if x == pivot]
            right = [x for x in array if x < pivot]
            return Sorting.quick_sort(left, reverse) + middle + Sorting.quick_sort(right, reverse)


numbers = [9,4,3,6,1,7,2,8,5]

if __name__ == "__main__":
        # print(Sorting.bubble_sort(numbers))
        # print(Sorting.bubble_sort(numbers, True))
        # print(Sorting.selection_sort(numbers, True))
        # print(Sorting.insertion_sort(numbers, True))
        # print(Sorting.merge_sort(numbers))
        print(Sorting.quick_sort(numbers, True))