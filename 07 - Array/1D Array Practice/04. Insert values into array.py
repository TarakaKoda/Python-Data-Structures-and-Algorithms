# 4. Insert value in an array using insert() method
from array import *

class Array:

    def insert_values_into_array(self):
        my_array = array('i',[1,2,3,4,5])
        print("Step 4")
        my_array.insert(3, 11)
        print(my_array)



if __name__ == "__main__":
    Array().insert_values_into_array()