# Nested even sum using recurion

class recursion:

    def nested_even_sum(self, obj):
        result = 0
        for key in obj:
            if isinstance(obj[key], int):
                if obj[key]%2 == 0:
                    result+= obj[key]
            else:
                if isinstance(obj[key], dict):
                    result += self.nested_even_sum(obj[key])
        return result

obj2 = {
  "a": 2,
  "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
  "c": {"c": {"c": 2}, "cc": 'ball', "ccc": 5},
  "d": 2,
  "e": {"e": {"e": 2}, "ee": 'car'}
}


if __name__ == "__main__":
    print(recursion().nested_even_sum(obj2))

