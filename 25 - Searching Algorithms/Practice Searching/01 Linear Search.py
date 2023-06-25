class Searching:
    @staticmethod
    def linear_search(arr, target):
        for i in range(len(arr)):
            if arr[i] == target:
                return i
        return -1  # Target element not found



if __name__ == "__main__":
    # Example usage
    my_list = [5,9,3,4,5,1,2,7]
    target_element = 2
    result = Searching.linear_search(my_list, target_element)
    if result != -1:
        print(f"Element {target_element} found at index {result}")
    else:
        print(f"Element {target_element} not found in the list")
