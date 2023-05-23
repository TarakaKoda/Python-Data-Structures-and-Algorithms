# convert numbers into string in a dictionary using recursion

class recursion:

    def stringify_number(self,obj):
        new_obj = obj
        for key in new_obj:
            if isinstance(new_obj[key], int):
                new_obj[key] = str(new_obj[key])
            if isinstance(new_obj[key], dict):
                new_obj[key] = self.stringify_number(new_obj[key])
        return new_obj

obj = {
    "num": 1,
    "test": [],
    "data": {
        "val": 4,
        "info": {
            "isRight": True,
            "random": 66
        }
    }
}


if __name__ == "__main__":
    print(recursion().stringify_number(obj))