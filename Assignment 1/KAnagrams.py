# Hashing the elements

# Time complexity is O(m + n)
# the function loops through both the first and second strings 
# once. Therefore the time complexity is dependent on the sum of the
# length of those two strings

# Space Complexity is O(1)
# given that there are only 128 possible characters that 
# can be used, the space used is constant relative to 
# the length of either string

#   Approach
#   1. useing an array of frequencies to record the frequency of 
#.     letters in first string
#   2. decrement the frequency of each character as processed in second string
#   3. if the difference of characters is greater than K return false
#   4. return tue otherwise
def KAnagrams(s1, s2, k):

    # checks for uneven lengths
    if len(s1) != len(s2):
        return False

    # frequency table
    freq = [0] * 128

    # indexes all the characters of the first string
    for curr in s1:
        freq[ord(curr)] += 1

    diff = 0
    # compares frequencies to the other string
    for curr in s2:

        freq[ord(curr)] -= 1

        # if there is a difference, record as a difference
        if freq[ord(curr)] < 0:
            diff += 1
        # check if there are two many differences
        if diff > k:
            return False

    return True

# False
print(KAnagrams("apple", "peach", 1))

# True
print(KAnagrams("apple", "peach", 2))

# True
print(KAnagrams("cat", "dog", 3))
    
# True
print(KAnagrams("debit curd", "bad credit", 1))

# False
print(KAnagrams("baseball", "basketball", 2))
