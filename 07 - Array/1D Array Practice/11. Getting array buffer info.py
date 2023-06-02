# 11. Get array buffer information through buffer_info()
from array import *

class Array:

    def get_array_buffer_info(self):
        my_array = array('i',[1,2,3,4,5])
        print("Step 11")
        print(my_array.buffer_info())



if __name__ == "__main__":
    Array().get_array_buffer_info()