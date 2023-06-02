# 5. Extend python array using extend() method
from array import *

class Array:

    def extending_array(self):
        my_array = array('i',[1,2,3,4,5])
        print("Step 5")
        my_array1 = array('i', [10, 11, 12])
        my_array.extend(my_array1)
        print(my_array)



if __name__ == "__main__":
    Array().extending_array()