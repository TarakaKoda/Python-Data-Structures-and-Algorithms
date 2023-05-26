# 7. Remove any array element using remove() method
from array import *

class Array:

    def removing_from_array_using_remove(self):
        my_array = array('i',[1,2,3,4,5])
        print("Step 7")
        my_array.remove(1)
        print(my_array)



if __name__ == "__main__":
    Array().removing_from_array_using_remove()