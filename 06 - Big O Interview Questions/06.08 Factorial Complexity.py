# What will be the complexity of this factorial code

class Big_O:
    '''
        def factorial(self, num): --------------------------------------> M(n)
        if num in [0,1]: ---------------------------------------> O(1)
                                                                      } = O(1)
            return num -----------------------------------------> O(1)
        else:
            return num * self.factorial(num-1) -----------------------> M(n-1)

        Calculating time complexity of the above recursive code

        M(n) = O(1) + M(n-1) ---------------> eq. 1
        M(0) = O(1) + M(0-1) => O(1) -------> eq. 2
        M(n-1) = O(1) + M((n-1)-1) ---------> eq. 3
        M(n-2) = O(1) + M((n-2)-1) ---------> eq. 4

        using eq. 3 in eq. 1,  we get
        M(n) = O(1) + O(1) + M((n-1)-1)
             = 1 + 1 + M(n -2)
             = 2 + M(n- 2) -----------------> using eq. 4 in this we get
             = 2 + O(1) + M((n-2)-1)
             = 2 + 1 + M(n-3)
             = 3 + M(n-3)
             replacing 3 with a, we get
             = a + M(n-a)
             = n + M(n-n) replacing a with n
             = n + 1 ------------------------> from eq. 2
             = n

        The Time Complexity of this Factorial code is O(n)
    '''

    def factorial(self, num):
        if num in [0,1]:
            return num
        else:
            return num * self.factorial(num-1)

if __name__ == "__main__":
    print(Big_O().__doc__)
    print(f"The output of the above factorial code: {Big_O().factorial(5)}")

