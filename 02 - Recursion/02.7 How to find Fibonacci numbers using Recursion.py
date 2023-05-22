class recursion:
    '''
      Fibonacci numbers - Recursion
      Fibonacci sequence is a sequence of numbers in which each number is sum of two preceding ones and sequence start with 0 and 1
      0,1,1,2,3,5,8,13,21,34,55,89,....
      f(n) = f(n-1)+f(n-1)
    '''

    def fibonacci(self,n: int) -> int:
        assert n >= 0 and int(n) == n, f"{n} must be a positive integer!"
        if n in [1,0]:
            return n
        else:
            return self.fibonacci(n-1) + self.fibonacci(n-2)


if __name__ == "__main__":
    print(recursion().__doc__)
    print(recursion().fibonacci(-2))


