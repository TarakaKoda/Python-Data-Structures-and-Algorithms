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