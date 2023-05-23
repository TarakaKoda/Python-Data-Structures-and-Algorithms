# Write a recursive program to find power

class recursion:

    def power(self,base, exp):
        assert int(exp) == exp and exp >= 0, "exp must be positive integer only!"
        if exp == 0:
            return 1
        if exp == 1:
            return base
        else:
            return base * self.power(base, exp-1)


if __name__ == "__main__":
    print(recursion().power(5, 3))


