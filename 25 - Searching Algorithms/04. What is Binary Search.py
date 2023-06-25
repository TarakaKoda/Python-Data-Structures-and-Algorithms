class Binary_Search:
    '''
    Binary search is an efficient algorithm used to search for a specific target value within a sorted array or list. It
    follows a divide-and-conquer approach, repeatedly dividing the search space in half until the target value is found
    or determined to be absent.

    Here's how the binary search algorithm works:

    Begin with a sorted array or list. Let's call it arr.

    Set two pointers, low and high, initially pointing to the first and last elements of the array, respectively.

    Calculate the middle index mid as (low + high) / 2.

    Compare the target value with the element at the middle index (arr[mid]):

    If the target value matches arr[mid], the search is successful, and the index of the target value is returned.
    If the target value is less than arr[mid], update high to mid - 1, and repeat from step 3 within the lower half of
    the array.
    If the target value is greater than arr[mid], update low to mid + 1, and repeat from step 3 within the upper half of
    the array.
    Repeat steps 3-4 until the target value is found or low becomes greater than high. In the latter case, the target
    value is not present in the array, and the search terminates.

    Binary search has a time complexity of O(log n), where n is the number of elements in the array. This makes it
    significantly faster than linear search algorithms, especially for large arrays. However, it requires the array to
    be sorted beforehand, as the algorithm relies on the ability to divide the search space in half at each step.
    '''