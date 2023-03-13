# Binary Search Variation

# time complexity is O(log n)
#
# This method of solving the problem, utilizes binary search. For a value to be "correct" for 
# a given index, the value at the index should be one greater than the index. For example at index
# 5 the correct value should be 6. By understanding this property, you can binary serach. You look
# to the left when lst[i] != i + 1 and you check right otherwise. By constantly dividing the array
# in half, you get a run time of O(log n)


# space complexity is O(1)
#
# this function uses constant space complexity. This is the case because the only extra memory
# we use are simple variables like left, right, and those are the only variables we will create
# regardless of the size of the list. This function also does not use any data structures that are 
# dependent on the size of the list


# Writeup
#
# I utilized a binary search in this problem. I described it a bit above in the time complexity 
# section. I start by looking at the middle element. lets call the index i. If the value at lst[i]
# is not equal to i + 1, you know the skip of a value had occured earlier in the list. Thus you move
# to the left half of the list. If the value of lst[i] is equal to i + 1, then the skipped
# value has yet to show up. This means you move to the right half of the list. This continued
# process narrows down the size of the possible values in the array to become smaller and smaller
# after each itteration. It cuts down the possible indices of the skip by half each itteration. 
# Eventually, youre only looking at a single value and you return that value.

# took 13 min

def MissingInteger(lst, n):
    
    # checks for edge case
    if lst == None or len(lst) == 0:
        return 0

    left = 0
    right = len(lst) - 1

    # keeps running while the 
    while left <= right:
        mid = (left + right) // 2


        if lst[mid] != mid + 1:
            right = mid - 1
        else:
            left = mid + 1

    return left + 1





# 5
print(MissingInteger([1, 2, 3, 4, 6, 7], 7))

# 2
print(MissingInteger([1], 2))

# 9
print(MissingInteger([1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12], 12))