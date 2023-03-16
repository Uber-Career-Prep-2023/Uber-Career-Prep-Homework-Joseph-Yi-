# Two pointers

# Time complexity is O(n)
# the loop itterates through the entire list once

# Space complexity is O(1)
# since the only additional space required is the dictionary 
# for the number of characters, there can only be 128 possible 
# characters

#   Approach
#   1. Created a set out of the list of required characters
#   2. creates a growing and shrinking window.
#   3. checks the substring if it contains all of the requried characters
#   4. compares the length of this substring and records the minimum

# this took 35 min
def shortestSubstring(s, req):
    required_chars = set(req)
    freq = {}
    left = 0
    right = 0
    minLen = float('inf')

    while right < len(s):
        curr = s[right]
        freq[curr] = freq.get(curr, 0) + 1
        right += 1

        while all(freq.get(curr, 0) >= 1 for curr in required_chars):
            minLen = min(minLen, right - left)
            left_char = s[left]
            freq[left_char] -= 1
            left += 1

    return minLen if minLen != float('inf') else 0

# 4
print(shortestSubstring("abracadabra", "abc"))

# 3
print(shortestSubstring("zxycbaabcdwxyzzxwdcbxyzabccbazyx", "zzyzx"))

# 3
print(shortestSubstring("dog", "god"))