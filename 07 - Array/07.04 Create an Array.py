class Array:
    '''
      Memory
      stored in contagious location next to each other
      Create an array
      - Assign it to a variable
      - Define the type of elements that it will store
      - Define the size(Maximum number of elements)
      from array import *
      arr = array(typecode,[initializers])
      typecode  C Type              Python type   Minimum Size in bytes  Notes
      'b'       Signed char         int           1
      'B'       Unsigned char       int           1
      'h'       signed short        int           2
      'H'       Unsigned short      int           2
      'i'       signed int          int           2
      'I'       Unsigned int        int           2
      'l'       signed long         int           4
      'L'       Unsigned long       int           4
      'q'       signed long long    int           8
      'Q'       Unsigned long long  int           8
      'f'       float               float         4
      'd'       double              float         8
      'u'       Py_UNICODE          Unicode character 2                     (1)
      Time - O(1)
      Space - O(n)
    '''


if __name__ == "__main__":
    print(Array().__doc__)