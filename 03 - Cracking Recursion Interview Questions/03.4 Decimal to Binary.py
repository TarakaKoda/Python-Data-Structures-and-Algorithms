#  How to convert a number from decimal to Binary using recursion?

def decimal_to_binary(num):
    assert int(num) == num, "num must be an integer"
    if num == 0:
        return 0
    else:
        return num%2 + 10 * decimal_to_binary(int(num/2))

print(decimal_to_binary(12))