class Big_O:
    '''
      How to measure the codes using Big O?
      Set of Rules:
      Rule 1 Any assignment statements and if statements that are executed once regqrdless og the size of the problem O(1)
      Rule 2 A sample for loop from 0 to n (with no internal loops) O(n)
      Rule 3 A nested loop of the same type takes Quadratic time complexity O(n^2)
      Rule 4 A loop in which controlling parameters is divided by two at each step )(log n)
      Rule 5 when dealing with multiple statements just add them up
    '''

if __name__ == "__main__":
    print(Big_O().__doc__)