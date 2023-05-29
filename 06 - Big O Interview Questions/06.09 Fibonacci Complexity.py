# What will be the complexity of the fibonacci code

class Big_O:
    '''
    def fibonacci(self, number):
        if number in [1,0]: --------------------------------------------------> O(1)
            return number ----------------------------------------------------> O(1)
        else:
            return self.fibonacci(number - 1) + self.fibonacci(number - 2) ---> O(2^n)

    As we learn the rules for calculating time complexity of a double recursive program is O(2^n)
    '''

    def fibonacci(self, number):
        if number in [1,0]:
            return number
        else:
            return self.fibonacci(number - 1) + self.fibonacci(number - 2)

if __name__ == "__main__":
    print(Big_O().__doc__)
    print(f"The output of the fibonacci code: {Big_O().fibonacci(5)}")
