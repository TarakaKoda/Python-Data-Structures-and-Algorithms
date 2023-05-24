# print pairs

class Big_O:

    def print_pairs(self,arr):
        for i in arr:
            for j in arr:
                print('(',i,',',j,')')
        print("The time complexity of above problem is O(n^2) Quadratic")

if __name__ == "__main__":
    Big_O().print_pairs([1,2,3,6])