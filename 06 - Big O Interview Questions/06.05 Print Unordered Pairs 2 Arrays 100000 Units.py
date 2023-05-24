# Print Unordered Pairs 2 Arrays 100000 Units

class Big_O:

    def problem(self,arr,arr1):
        for i in range(0,len(arr)):
            for j in range(0,len(arr1)):
                for k in range(0,100000):
                    print('(',i,',',j,')')
        print("The time complexity of above problem is O(len(arr)*len(arr1))")

if __name__ == "__main__":
    Big_O().problem([1,2], [3,4])