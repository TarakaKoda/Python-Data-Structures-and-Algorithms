# check whether a string is palindrome or not

class recursion:

    def is_palindrome(self,string):
        if len(string) == 0:
            return True
        if string[0] != string[-1]:
            return False
        else:
            return self.is_palindrome(string[1:-1])


if __name__ == "__main__":
    print(recursion().is_palindrome("markram"))