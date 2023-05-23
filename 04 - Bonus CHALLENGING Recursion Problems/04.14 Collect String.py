# Collect all the string from a dictionary using recursion

class recursion:

    def collect_string(self, obj):
        result = []
        for key in obj:
            if isinstance(obj[key], str):
                result.append(obj[key])
            else:
                if isinstance(obj[key], dict):
                    return result + self.collect_string(obj[key])

        return result

obj1 = {
    "stuff": 'foo',
    "data": {
        "val": {
            "thing": {
                "info": 'bar',
                "moreInfo": {
                    "evenMoreInfo": {
                        "weMadeIt": 'baz'
                    }
                }
            }
        }
    }
}

if __name__ == "__main__":
    print(recursion().collect_string(obj1))
