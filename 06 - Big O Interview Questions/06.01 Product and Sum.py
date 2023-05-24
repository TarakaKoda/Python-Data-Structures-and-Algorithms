# product and sum of an array

class Big_O:

    def sum_and_product(self,arr):
        sum = 0
        product = 1
        for i in arr:
            sum+=i
        for i in arr:
            product *= i
        print("The time complexity of above the problem is O(n)")

if __name__ == "__main__":
    Big_O().sum_and_product([1,5,6])