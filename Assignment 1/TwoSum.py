# Hash the elements

# Time complexity is O(n)
# the function loops throuhg all values of the array once

# Space complexity is O(n)
# the function creates a hash of all occurences of values

#   Approach
#   1. itterate over the integers over the array
#   2. check if the complementory value is in the hash
#   3. incremenet by existing amount of complementary value

# this took me 7 min




def TwoSum(arr, targetSum):
    freq = {}
    count = 0
    
    # itterate through array
    for x in arr:
        
        # checks the hash for the complementary value
        if targetSum - x in freq:
            # increments  by the total number of that complementary value
            count += freq[targetSum - x]
        
        # adds the current value to the hash
        freq[x] = freq.get(x, 0) + 1
    
    return count

# 2
print(TwoSum([1, 2, 3, 4, 5], 6))

# 3
print(TwoSum([1, 1, 2, 3, 4, 5], 6))

# 0
print(TwoSum([1, 2, 3, 4, 5], 10))

# 0
print(TwoSum([], 6))

print()

# 3
print(TwoSum([1, 10, 8, 3, 2, 5, 7, 2, -2, -1], 10))

# 3
print(TwoSum([1, 10, 8, 3, 2, 5, 7, 2, -2, -1], 8))

# 5
print(TwoSum([4, 3, 3, 5, 7, 0, 2, 3, 8, 6], 6))