# 12. Check for number of occurrences of an element using count() method
from array import *

class Array:

    def counting_number_of_occurrences_using_count(self):
        my_array = array('i',[1,2,3,4,5])
        print("Step 12")
        my_array.append(1)
        print(my_array.count(1))
        print(my_array)



if __name__ == "__main__":
    Array().counting_number_of_occurrences_using_count()