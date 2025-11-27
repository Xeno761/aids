# Quick Sort using Divide & Conquer
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]                      # choose first element as pivot
    left = [x for x in arr[1:] if x <= pivot]   # smaller elements
    right = [x for x in arr[1:] if x > pivot]   # bigger elements

    return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort([4,2,6,9,1]))
