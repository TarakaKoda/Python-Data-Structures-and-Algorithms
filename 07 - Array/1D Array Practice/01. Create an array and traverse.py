# 1. Create an array and traverse.
from array import *

class Array:

    def create_array_and_traverse(self):
        my_array = array('i',[1,2,3,4,5])
        for i in my_array:
            print(i)



if __name__ == "__main__":
    Array().create_array_and_traverse()
