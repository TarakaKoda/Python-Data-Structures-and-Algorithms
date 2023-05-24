# Print Unordered Pairs 2 Arrays

class Big_O:

    def undereed_pairs_two_arr(self,arr,arr1):
        for i in range(0,len(arr)):
            for j in range(0,len(arr1)):
                if arr[i] < arr[j]:
                    print('(',i,',',j,')')
        print("The time complexity of above problem is O(len(arr)*len(arr1))")


if __name__ == "__main__":
    Big_O().undereed_pairs_two_arr([2,3],[4,6])
