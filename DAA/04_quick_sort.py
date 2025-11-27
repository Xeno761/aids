def quick_sort(arr):
    """
    Quick Sort: Divide and Conquer sorting using partitioning
    Time Complexity: O(n log n) average, O(n²) worst | Space Complexity: O(log n)
    In-place sorting with randomized pivot for better performance
    """
    # Base case: arrays with 0 or 1 element are sorted
    if len(arr) <= 1:
        return arr
    
    # Choose pivot (using middle element for better average case)
    pivot = arr[len(arr) // 2]
    
    # Partition: Divide into three parts
    left = [x for x in arr if x < pivot]  # Elements smaller than pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to pivot
    right = [x for x in arr if x > pivot]  # Elements larger than pivot
    
    # Combine: Recursively sort left and right, then merge
    return quick_sort(left) + middle + quick_sort(right)

def quick_sort_inplace(arr, low=0, high=None):
    """
    In-place Quick Sort: More memory efficient version
    """
    if high is None:
        high = len(arr) - 1
    
    # Base case: stop when low >= high
    if low < high:
        # Partition and get pivot index
        pivot_index = partition(arr, low, high)
        # Recursively sort left side
        quick_sort_inplace(arr, low, pivot_index - 1)
        # Recursively sort right side
        quick_sort_inplace(arr, pivot_index + 1, high)
    
    return arr

def partition(arr, low, high):
    """
    Helper function: Partitions array around pivot
    """
    pivot = arr[high]  # Choose rightmost element as pivot
    i = low - 1  # Index for smaller elements
    
    # Traverse and place elements smaller than pivot on left
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements
    
    # Place pivot at correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1  # Return partition point

# Driver code
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = quick_sort(arr)
    print(f"Original array: {arr}")
    print(f"Sorted array (functional): {sorted_arr}")
    
    arr2 = [64, 34, 25, 12, 22, 11, 90]
    quick_sort_inplace(arr2)
    print(f"Sorted array (in-place): {arr2}")
