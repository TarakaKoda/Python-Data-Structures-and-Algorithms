# capitalize first word of the array using recursion

class recursion:

    def capitalize_first(self,arr):
        result = []
        if len(arr) == 0:
            return result
        else:
            result.append(arr[0][0].upper() + arr[0][1:])
            return result + self.capitalize_first(arr[1:])


if __name__ == "__main__":
    print(recursion().capitalize_first(["i", "am", "srinu"]))
