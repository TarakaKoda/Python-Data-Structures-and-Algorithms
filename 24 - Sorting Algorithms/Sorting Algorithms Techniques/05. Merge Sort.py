class Merge:
    '''

      Merge Sort
      - It is a divide and conquer algorithm
      - Divide the input array in two halves and we keep having recursively untill they become too small that cannot be broken further
      - merge halves by sorting them
      Time O(nlogn) space O(n)
      merge sort is out place alogithm
      merge sort is stable
      when to use merge sort?
      - when you need stable sort
      - when average expexted time in O(NlogN)
      when to avoid stable sort?
      - when space is a concern
    '''



    def merge(self,values,left,middle,right):
      n1 = middle - left + 1
      n2 = right-middle
      l = [0] * n1
      r = [0] * n2
      for i in range(0,n1):
        l[i] = values[left+i]
      for i in range(0,n2):
        r[i] = values[middle+1+i]
      i=0
      j=0
      k=l
      while i <n1 and j < n2:
        if l[i] <= r[j]:
          values[k] = l[i]
          i+=1
        else:
          values[k] = r[j]
          j+=1
        k+=1
      while i < n1:
        values[k] =l[i]
        i+=1
        k+=1
      while j < n1:
        values[k] =l[j]
        j+=1
        k+=1
    def sort(self,values,l,r):
       if l < r:
        m = (l+(r-1))//2
        self.sort(values,l,m)
        self.sort(values,m+1,r)
        self.merge(values,l,m,r)
