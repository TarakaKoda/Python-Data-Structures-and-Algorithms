# 14. Convert array to a python list with same elements using tolist() method
from array import *

class Array:

    def array_to_list(self):
        my_array = array('i',[1,2,3,4,5])
        print("Step 14")
        print(my_array.tolist())



if __name__ == "__main__":
    Array().array_to_list()