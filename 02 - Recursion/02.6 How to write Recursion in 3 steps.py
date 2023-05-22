class recursion:
    '''
     Factorial - Product of all positive integers less than or equal to n. Denoted by n!. Only positive numbers. 0! = 1.
      Step 1: Recursive Case - the flow
      n! = n*(n-1)*(n-2)*(n-3)*.....*2*1
      n! = n*(n-1)!

      Step 2: Base case - the stopping criterion
      0! = 1
      1! = 1

      Step3: Unintentional case - the constraint
      n>0
    '''

if __name__ == "__main__":
    print(recursion().__doc__)
