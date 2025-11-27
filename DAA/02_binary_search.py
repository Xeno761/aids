def binary_search(arr, target):
    """
    Binary Search: Finds target in sorted array by dividing search space in half
    Prerequisites: Array must be SORTED
    Time Complexity: O(log n) | Space Complexity: O(1)
    """
    left = 0  # Starting index
    right = len(arr) - 1  # Ending index
    
    # Loop while search space exists
    while left <= right:
        mid = (left + right) // 2  # Calculate middle index
        
        # If element is at middle, return index
        if arr[mid] == target:
            return mid
        # If target is smaller, search left half
        elif arr[mid] > target:
            right = mid - 1
        # If target is larger, search right half
        else:
            left = mid + 1
    
    # If not found, return -1
    return -1

# Driver code
if __name__ == "__main__":
    sorted_arr = [10, 20, 30, 40, 50, 60, 70, 80]
    target = 50
    result = binary_search(sorted_arr, target)
    
    if result != -1:
        print(f"Element found at index: {result}")
    else:
        print("Element not found in array")
