class Binary_Search:
    @staticmethod
    def binary_search(arr, target):
        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return -1  # Target value not found

# Example usage
my_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
target_value = 12

result = Binary_Search.binary_search(my_list, target_value)

if __name__ == "__main__":
    # Example usage
    my_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    target_value = 12

    if result != -1:
        print(f"Target value {target_value} found at index {result}")
    else:
        print("Target value not found in the list.")
