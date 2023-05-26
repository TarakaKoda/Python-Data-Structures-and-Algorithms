# 13. Convert array to string using tostring() method
from array import *

class Array:

    def array_to_string(self):
        my_array = array('i',[1,2,3,4,5])
        print("Step 13")
        strTemp = my_array.tostring()
        print(strTemp)
        ints = array('i')
        ints.fromstring(strTemp)
        print(ints)



if __name__ == "__main__":
    Array().array_to_string()