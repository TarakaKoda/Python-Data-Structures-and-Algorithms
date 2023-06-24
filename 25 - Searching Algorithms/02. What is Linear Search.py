class Linear_Search:
    '''
    Linear search, also known as sequential search, is a simple searching algorithm that scans through a list or array
    sequentially to find a specific target element. Here's how linear search works:

    Start at the beginning of the list or array.

    Compare the target element with the current element.

    If a match is found, return the index of the element.

    If the target element is not found, move to the next element and repeat steps 2 and 3.

    Continue this process until the target element is found or the end of the list is reached.

    If the target element is not found in the list, return a sentinel value or indicate that the element is not present.

    Linear search is straightforward to implement, but it has a time complexity of O(n) in the worst case, where n is
    the size of the list. This means that the time it takes to perform the search grows linearly with the size of the list.
    '''

if __name__ == "__main__":
    print(Linear_Search().__doc__)

