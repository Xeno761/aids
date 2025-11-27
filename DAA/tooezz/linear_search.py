# Linear Search
def linear_search(arr, key):
    for i in range(len(arr)):      # check every element
        if arr[i] == key:          # if key is found
            return i               # return index
    return -1                      # not found

print(linear_search([4, 2, 9, 1], 9))
