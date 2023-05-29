# calculate the time complexity of power of 2 code

class Big_O:
    '''
        def power_of_2(self, num):
        if num in [1, 0]: ------------------------------> O(1)
            return num ---------------------------------> O(1)
        else:
            prev = self.power_of_2(int(num)//2)----------------> O(log n): As you see in this algorithm, in each state,
                                                                           we divide our iteration into two.
                                                                           So, we can say its logarithmic complexity

            curr = 2*prev ------------------------------> O(1)
            print(curr) --------------------------------> O(1)
            return curr --------------------------------> O(1)
    '''

    def power_of_2(self, num):
        if num in [1, 0]:
            return num
        else:
            prev = self.power_of_2(int(num)//2)
            curr = 2*prev
            print(curr)
            return curr

if __name__ == "__main__":
    print(Big_O().__doc__)
    Big_O().power_of_2(50)