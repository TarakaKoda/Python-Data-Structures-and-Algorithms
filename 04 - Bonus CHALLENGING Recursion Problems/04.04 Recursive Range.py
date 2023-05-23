# Recursive range 1
class recursion:

    def recursive_range(self, num):
        assert int(num) == num and num >= 0, "num must be positive integer only!"
        if num in [0,1]:
            return num
        else:
            return num + self.recursive_range(num-1)

    def recursive_range_with_start_stop_step(self, start, stop, step=1):
        if start >= stop:
            return []
        else:
            return [start] + self.recursive_range_with_start_stop_step(start+step, stop, step)


if __name__ == "__main__":
    print(recursion().recursive_range(4))
    print(recursion().recursive_range_with_start_stop_step(1, 10, 2))



