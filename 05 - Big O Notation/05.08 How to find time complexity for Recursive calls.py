class Big_O:
    '''

Finding the time complexity of recursive calls involves analyzing the number of recursive calls made and the work done
in each call. Here's a step-by-step approach to determining the time complexity of recursive algorithms:

    1. Identify the recurrence relation: A recurrence relation describes the number of times the recursive function is
       called. It typically involves a recursive call and any additional operations performed within the function.
       Write down the recurrence relation for your algorithm.

    2. Determine the base case: The base case specifies the condition under which the recursive calls terminate and
       return a result without further recursion. It is essential for analyzing the time complexity. Identify the base
       case(s) in your algorithm.

    3. Solve the recurrence relation: To find the time complexity, you need to solve the recurrence relation. This step
       may involve various methods depending on the complexity of the relation. Some common techniques include
       substitution, recursion trees, and the master theorem.

    4. Analyze the dominant term: Once you have solved the recurrence relation, you will obtain a mathematical
       expression involving variables such as n (input size) and possibly other constants. Analyze the dominant term of
       the expression, which represents the most significant factor in determining the time complexity. Ignore
       lower-order terms and constants.

    5. Express the time complexity: Finally, express the time complexity using big O notation. The dominant term
       obtained from the previous step represents the time complexity of your recursive algorithm.
    '''

if __name__ == "__main__":
    print(Big_O().__doc__)