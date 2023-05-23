# find the product of the given array using recursion

class recursion:

    def product_of_array(self,arr):
        if len(arr) == 1:
            return arr[0]
        else:
            return arr[0] * self.product_of_array(arr[1:])


if __name__ == "__main__":
    print(recursion().product_of_array([2, 1, 9]))



