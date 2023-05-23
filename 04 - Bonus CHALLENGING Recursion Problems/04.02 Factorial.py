# Find the factorial of the given number using recursion

class recursion:

    def factorial(self, num):
        assert num >= 0 and int(num) == num, "num must be positive integer only!"
        if num in [0,1]:
            return num
        else:
            return num * self.factorial(num-1)


if __name__ == "__main__":
    print(recursion().factorial(4))