# reverse a string using recursion

class recursion:

    def reverse(self,string):
        if len(string) == 1:
            return string
        else:
            return string[-1] + self.reverse(string[:-1])

if __name__ == "__main__":
    print(recursion().reverse("srinu"))