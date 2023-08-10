# DP Marking

# Time complexity is O(n^2)
# the out loop itereates n times witht he inner loop iterating
# upwards of n times thus O(N^2)

# Space complexity is O(n)
# the dp array is dependent on the size of the input string

# This took me 27 min
def wordBreak(s, word_dict):
    # takes care of upper and lower case
    s = s.lower()
    word_dict = set(word.lower() for word in word_dict)
    
    n = len(s)
    # creates a dp of the length of the original string
    dp = [False] * (n + 1)
    dp[0] = True

    # checks at each letter if there is a word that exists in the dictionary
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_dict:
                dp[i] = True
                break

    return dp[n]

# Test cases
word_dict = {"Elf", "Go", "Golf", "Man", "Manatee", "Not", "Note", "Pig", "Quip", "Tee", "Teen"}

print(wordBreak("mangolf", word_dict))        # Output: True
print(wordBreak("manateenotelf", word_dict))  # Output: True
print(wordBreak("quipig", word_dict))         # Output: False
