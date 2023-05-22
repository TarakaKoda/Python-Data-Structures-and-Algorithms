# How to find GCD(the greatest common divisor) of two numbers using recursion?

def gcd(a: int, b: int) -> int:
    assert int(a) == a and int(b) == b, f"{a} and {b} must be integer values"
    if a < 0:
        a *= -1
    if b < 0:
        b *= -1
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

print(gcd(14, -6))
