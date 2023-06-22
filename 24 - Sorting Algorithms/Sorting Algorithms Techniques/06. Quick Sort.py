class Quick:
    '''
         Quick Sort
         - Quick sort is a divide and conquer algorithm
         - Find pivot number and make sure smaller numbers located at left of pivot and bigger numbers are located at right of pivot
         - unlike merge sort algorithm extra space is not required
         Time O(nLogin) space O(n)
         Quick sort is unstable sorting algorithm
         Quick sort is inn place sorting algorithm

         When to use Quick sort algorithm?
         - When average expected time is O(nlogn)
         when to avoid Quick sort algorithm?
         - When space is a concern
         - when you seed stable sort algorithm
       '''

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