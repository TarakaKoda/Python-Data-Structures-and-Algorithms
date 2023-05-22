# How to find the sum of digits of a +ve integer number using recursion?

def sum_of_digits(n: int) -> int:
    assert n >= 0 and int(n) == n, f"{n} must be positive integer only!"
    if n in [1,0]:
        return n
    else:
        return n%10 + sum_of_digits(int(n/10))

print(sum_of_digits(27))