def TwoSum(arr, k):
    freq = {}
    count = 0
    
    for x in arr:
        
        if k - x in freq:
            count += freq[k - x]
        
        freq[x] = freq.get(x, 0) + 1
    
    return count

# 2
print(TwoSum([1, 2, 3, 4, 5], 6))

# 2
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