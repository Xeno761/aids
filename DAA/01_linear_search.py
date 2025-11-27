def linear_search(arr, target):
    """
    Linear Search: Finds target element by checking each element sequentially
    Time Complexity: O(n) | Space Complexity: O(1)
    """
    # Iterate through each element in the array
    for i in range(len(arr)):
        # If element matches target, return its index
        if arr[i] == target:
            return i
    # If not found, return -1
    return -1

# Driver code - Test the function
if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50, 60]
    target = 30
    result = linear_search(arr, target)
    
    if result != -1:
        print(f"Element found at index: {result}")
    else:
        print("Element not found in array")
