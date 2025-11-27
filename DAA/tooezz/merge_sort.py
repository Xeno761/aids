# Merge Sort (Divide & Conquer)
def merge_sort(arr):
    if len(arr) <= 1:                 # base condition
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])      # sort left half
    right = merge_sort(arr[mid:])     # sort right half

    return merge(left, right)         # merge both halves


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):   # compare elements
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])           # append remaining elements
    result.extend(right[j:])
    return result

print(merge_sort([5,3,8,1,2]))
