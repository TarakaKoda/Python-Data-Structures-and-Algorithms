# Print Unordered Pairs

class Big_O:

    def unordered_pairs(self,arr):
        for i in range(0,len(arr)):
            for j in range(0,len(arr)):
                print('(',i,',',j,')')
        print("The time complexity of above problem is O(n^2) Quadratic")


if __name__ == "__main__":
    Big_O().unordered_pairs([2,3,4])