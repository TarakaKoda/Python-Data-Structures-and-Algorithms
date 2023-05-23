# Find the fibonacci series using recursion

class recursion:

    def fibonacci(self, num):
        assert int(num) == num and num >= 0, "num must be an positive integer only!"
        if num in [1,0]:
            return num
        else:
            return self.fibonacci(num-1) + self.fibonacci(num-2)


if __name__ == "__main__":
    print(recursion().fibonacci(6))