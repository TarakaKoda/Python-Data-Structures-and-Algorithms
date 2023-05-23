# flatten using recursion

class recursion:

    def flatten(self,arr):
        result = []
        for items in arr:
            if isinstance(items, list):
                result.extend(self.flatten(items))
            else:
                result.append(items)
        return result


if __name__ == "__main__":
    print(recursion().flatten([2,[3,4,5],[9]]))

