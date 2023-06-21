class Hashing:
    '''
    Hash Functions
    - Mod Function
       def mod(number,cellNumber):
         return number%cellNumber

    - ASCII function
        def modAscii(string, cellNumber):
            total = 0
            for i in string:
                total += ord(i)
            return total % cellNumber

    Properties of good hash function
    - It distributes hash values uniformly across hash tables
    - It has to use all input data


    '''


def mod(number, cellNumber):
    return number % cellNumber

def modAscii(string, cellNumber):
    total = 0
    for i in string:
        total += ord(i)
    return total % cellNumber



if __name__ == "__main__":
    print(Hashing().__doc__)
    print(mod(400, 15))
    print(mod(123, 15))
    print(modAscii("ABC", 24))
    print(modAscii("CDE", 24))