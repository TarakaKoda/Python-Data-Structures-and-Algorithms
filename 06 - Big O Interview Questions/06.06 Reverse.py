# Reverse

class Big_O:

    def reverse(self,arr):
        for i in range(0,int(len(arr)/2)):
            other = len(arr)-i-1
            temp = arr[i]
            arr[i]=arr[other]
            arr[other]=temp
        print(arr)
        print("The time complexity of above problem is O(len(arr))")


if __name__ == "__main__":
    Big_O().reverse(["srinu"])