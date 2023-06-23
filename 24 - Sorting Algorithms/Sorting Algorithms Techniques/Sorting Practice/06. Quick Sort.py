class Quick:

    def partition(self, values, low, high):
        i = low - 1
        pivot = values[high]
        for j in range(low, high):
            if values[j] <= pivot:
                i += 1
                values[i], values[j] = values[j], values[i]
        values[i + 1], values[high] = values[high], values[i + 1]
        return i + 1

    def sort(self, values, start, end):
        if start < end:
            partition = self.partition(values, start, end)
            self.sort(values, start, partition - 1)
            self.sort(values, partition + 1, end)


    @staticmethod
    def quick_sort(array):
        if len(array) <= 1:
            return array
        else:
            pivot = array[len(array)//2]
            left = [x for x in array if x < pivot]
            middle = [x for x in array if x == pivot]
            right = [x for x in array if x > pivot]
            return Quick.quick_sort(left) + middle + Quick.quick_sort(right)

numbers = [2,-1,0,1,4,6,3,7,9,8]

if __name__ == "__main__":
    print(Quick.quick_sort(numbers))