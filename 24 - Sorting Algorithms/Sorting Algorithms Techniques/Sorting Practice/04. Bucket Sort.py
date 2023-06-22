import math
class Bucket:

    def __init__(self):
        self.insertion = Bucket.insertion_sort

    def sort(self, values):
        buckets = round(math.sqrt(len(values)))
        maxValue = max(values)
        arr = []
        for i in range(buckets):
            arr.append([])
        for i in values:
            index = math.ceil((i * buckets) / maxValue)
            arr[index - 1].append(i)
        for i in arr:
            self.insertion(i)
        values = [i for j in arr for i in j]
        return values

    @staticmethod
    def insertion_sort(array, reverse=False):
        if not reverse:
            for i in range(1, len(array)):
                key = array[i]
                j = i - 1
                while j>= 0 and key < array[j]:
                    array[j+1] = array[j]
                    j -= 1
                array[j+1] = key
        return array



if __name__ == '__main__':
    bucket = Bucket()
    lis = [5, 3, 7, 9, 10]
    lis = bucket.sort(lis)
    print(lis)


