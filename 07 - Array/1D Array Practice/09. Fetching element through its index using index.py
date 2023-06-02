# 9. Fetch any element through its index using index() method
from array import *

class Array:

    def fetch_any_element_through_its_index_using_index(self):
        my_array = array('i',[1,2,3,4,5])
        print("Step 9")
        print(my_array.index(2))



if __name__ == "__main__":
    Array().fetch_any_element_through_its_index_using_index()