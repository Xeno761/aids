# Binary Search (Iterative)
def binary_search(arr, key):
    low, high = 0, len(arr)-1

    while low <= high:                 # repeat until range is valid
        mid = (low + high) // 2        # middle index
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:           # search right half
            low = mid + 1
        else:                          # search left half
            high = mid - 1

    return -1

print(binary_search([1,2,3,4,5], 4))
