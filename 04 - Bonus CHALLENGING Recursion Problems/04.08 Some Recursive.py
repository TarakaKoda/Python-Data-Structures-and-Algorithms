# To check if a list of arr numbers contains odd numbers or not using callback function

class recursion:

    def some_recursion(self,arr, cb):
        if len(arr) <1:
            return False
        if not(cb(arr[0])):
            return self.some_recursion(arr[1:], cb)
        else:
            return True

    @staticmethod
    def is_odd(number):
        if number % 2 != 0:
            return True
        else:
            return False

if __name__ == "__main__":
    print(recursion().some_recursion([2,6,4], recursion.is_odd))


