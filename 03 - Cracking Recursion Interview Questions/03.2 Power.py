# How to calculate power of number using recursion?

def power(base: int, exp: int) -> int:
    assert exp >= 0 and int(exp) == exp, "exp must be positive integer only!"
    if exp == 0:
        return 1
    if exp == 1:
        return base
    else:
        return base * power(base, exp-1)

print(power(5,2))