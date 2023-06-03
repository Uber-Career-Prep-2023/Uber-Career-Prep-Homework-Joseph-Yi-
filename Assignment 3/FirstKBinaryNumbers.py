# Queue

# Space Complexity is O(k)
# this function requries k space for the resulting array
# and stores future binary numbers upwards of 2k. The total space
# complexity is 3k however this is just O(k)


# Time complexity is O(k) 
# the function loops k times, with each loop doing a constant amount of work
# resulting in a time complexity of O(k)

# Approach
# I start with the base csae of zero in the resulting array. I use an queue
# to show all the furture binary numbers in the sequence. We then iterate through a loop
# k times, each time popping an element from the queue and adding it to the resulting array.
# we allso append the next 2 possible future numbers after the current number onto the queue. 
# This queue acts more similarly to a suffix tree, having each path following specific binary
# options of 1 or 0.

# This problem took me 17 min

def FirstKBinaryNumbers(k):
    if k <= 0:
        return []

    # start with zero
    result = ['0']

    # initiate queue with the next binary number
    queue = ['1']

    while len(result) < k:
        binary_number = queue.pop(0)
        result.append(binary_number)

        # Generate the next binary numbers by appending '0' and '1' to the current number
        queue.append(binary_number + '0')
        queue.append(binary_number + '1')
        
        

    return result


print(FirstKBinaryNumbers(5))
print(FirstKBinaryNumbers(10))
