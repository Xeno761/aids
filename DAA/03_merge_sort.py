def merge_sort(arr):
    """
    Merge Sort: Divide and Conquer sorting algorithm
    Time Complexity: O(n log n) in all cases | Space Complexity: O(n)
    Stable sort that maintains relative order of equal elements
    """
    # Base case: arrays with 0 or 1 element are already sorted
    if len(arr) <= 1:
        return arr
    
    # Divide: Split array into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # Conquer: Recursively sort both halves
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    
    # Combine: Merge the sorted halves
    return merge(left_sorted, right_sorted)

def merge(left, right):
    """
    Helper function: Merges two sorted arrays into one sorted array
    """
    result = []  # Store merged elements
    i = j = 0  # Pointers for left and right arrays
    
    # Compare elements from both arrays and add smaller one
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements from left array
    result.extend(left[i:])
    # Add remaining elements from right array
    result.extend(right[j:])
    
    return result

# Driver code
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = merge_sort(arr)
    print(f"Original array: {arr}")
    print(f"Sorted array: {sorted_arr}")
