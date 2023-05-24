# Find the maximum number using recursion

def findMaxRecur(self, arr, n):
    if n == 1:
        return arr[0]
    else:
        return max(arr[n - 1], self.findMaxRecur(arr, n - 1))

