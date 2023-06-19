class Binary_Heap:
    '''
      Why do we need a binary heap?
      Find the min or max number among a set of numbers in logN time. And also we want to make sure that inserting doesnot take more than O(logN) time.
      Possible solutions
      - Store the numbers in a sorted array
      Find Min O(1)
      Insert O(n)
      store the numbers in a sorted manner in linked list
      Find Min O(1)
      Insert O(n)

      Practical Algorithm
      - Prim's algorithm
      - Heap Sort
      - Proprity Queue

      Types of binary heap
      Min Heap - the values of each node is less than or equal to the value of both its children
      max heap - it is exactly opposite of min heap that is value of each node is more than or equal to the value of both its children
    '''