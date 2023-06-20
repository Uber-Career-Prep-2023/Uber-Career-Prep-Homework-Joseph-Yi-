# Array

# Space Complexity is O(n)
# The words array is split on spaces thus dependent on the length
# of the input string

# Time complexity is O(n)
# the reversing of the list is O(n) time

# Approach
# You split based off spaces. Then reverse the list and join again

# This took me  min

def ReverseWords(string):

    words = string.split()
    
    rev = words[::-1]
    
    output = ' '.join(rev)
    
    return output


print(ReverseWords("Uber Career Prep"))

print(ReverseWords("Emma lives in Brooklyn, New York."))