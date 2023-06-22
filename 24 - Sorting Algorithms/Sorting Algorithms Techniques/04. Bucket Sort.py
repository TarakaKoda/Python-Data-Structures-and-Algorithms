import math
class Bucket:
    '''
    Bucket sort
      - Create buckets and distribute elements of array into buckets
      - sort buckets individually
      - merge buckets after sorting
      Number of buckets = round(sqrt(number of elements))
      Appropriate bucket = ceil(Value*number of bucket/MaxValue)
      Time O(N^2) Space - O(N)
      Bucket sort is out place sorting algorithm
      Bucket sort is stable, if the underlying sort is also stable

    When to use bucket sort?
      - when input is uniformly distributed over range
    when to avoid it?
      - when space is a concern
    '''

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
    print(Bucket.__doc__)
    bucket = Bucket()
    lis = [5, 3, 7, 9, 10]
    lis = bucket.sort(lis)
    print(lis)


