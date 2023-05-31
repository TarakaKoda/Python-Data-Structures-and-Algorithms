class Tuple:
    '''
       Tuple                                                                          List
    Immutable                                                                        Mutable
    We can reassign entire tuple but not change the elements in the tuple
    these methods cannot be used in tuple but list
    - append()
    - insert()
    - remove()
    - pop()
    - clear()
    - sort()
    - reverse()
    Tuples can be stored in Lists
    Lists can be stored in Tuples
    Both tuples and lists can be nested
    We generally ise tuples for heterogeneous(different) data types and lists for homogeneous(similar) data types
    Iterating through a tuple is faster than with list
    Tuple that contain immutable elements can be used as a key for dictionary
    If you have data that doesn't change, implementing it as tuple will be  guarantee that it remains write-protected
    '''


if __name__ == "__main__":
    print(Tuple().__doc__)