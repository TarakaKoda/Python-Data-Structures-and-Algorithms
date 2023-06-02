# 15. Slice Elements from an array
from array import *

class Array:

    def slice_elements_from_array(self):
        my_array = array('i',[1,2,3,4,5])
        print("Step 15")
        print(my_array[:])



if __name__ == "__main__":
    Array().slice_elements_from_array()