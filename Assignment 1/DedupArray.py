# Sort the array then solve

# Time complexity is O(n)
# the function only itterates through the loop once

# Space Complexity is O(1)
# the only extra space required are some variables
# which would be the same size independent of the size of input

#   Approach
#   1. Check if the array's last value is repeated 
#   2. Deletes if not unique

# this took me 5 min

def dedup_array(arr):
    if not arr:
        return []
    repeat = arr[0]
    i = 1

    # loops through array
    while i < len(arr):

        # checks if the value is repeated
        if arr[i] == repeat:
            del arr[i]
        else:
            # changes the new repeated value
            repeat = arr[i]
            i += 1
    return arr
