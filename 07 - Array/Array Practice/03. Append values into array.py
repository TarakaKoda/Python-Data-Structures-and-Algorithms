# 3. Append any value to the array using append() method
from array import *

class Array:

    def append_values_into_array(self):
        my_array = array('i',[1,2,3,4,5])
        print("Step 3")
        my_array.append(6)
        print(my_array)



if __name__ == "__main__":
    Array().append_values_into_array()