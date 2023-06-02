# 8. Remove last array element using pop() method
from array import *

class Array:

    def removing_from_array_using_pop(self):
        my_array = array('i',[1,2,3,4,5])
        print("Step 8")
        my_array.pop()
        print(my_array)



if __name__ == "__main__":
    Array().removing_from_array_using_pop()