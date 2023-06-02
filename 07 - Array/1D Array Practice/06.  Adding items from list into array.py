# 6. Add items from list into array using fromlist() method
from array import *

class Array:

    def adding_items_from_list_into_array(self):
        my_array = array('i',[1,2,3,4,5])
        print("Step 6")
        tempList = [20, 21, 22]
        my_array.fromlist(tempList)
        print(my_array)



if __name__ == "__main__":
    Array().adding_items_from_list_into_array()