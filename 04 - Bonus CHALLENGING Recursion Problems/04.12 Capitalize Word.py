# Capitalize word using recursion

class recursion:

    def capitalize_words(self, arr):
        result = []
        if len(arr) == 1:
            return [arr[0].upper()]
        else:
            result.append(arr[0].upper())
            return result + self.capitalize_words(arr[1:])

if __name__ == "__main__":
    print(recursion().capitalize_words(["srinu","pavan","naruto"]))