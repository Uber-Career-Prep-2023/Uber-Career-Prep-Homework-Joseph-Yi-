# two stack approach

# time is O(m + n)
# it must itterate through the length of both strings

# space is O(m + n)
# it must keep a stack that is dependent on the size of both strings

#   Approach
#   1. append all new non '#' characters onto the stack
#   2. pop the character at the top of the stack when character is a '#'

# this took 6 min


def BackspaceStringCompare(s1, s2):
    word1 = []
    word2 = []

    # Type first string
    for curr in s1:
        if curr == '#':
            if word1:
                word1.pop()
        else:
            word1.append(curr)

    # Type second string
    for curr in s2:
        if curr == '#':
            if word2:
                word2.pop()
        else:
            word2.append(curr)

    # Compare resulting text
    return word1 == word2


# true
print(BackspaceStringCompare("abcde", "abcde"))

# true
print(BackspaceStringCompare("Uber Career Prep", "u#Uber Careee#r Prep"))

# true
print(BackspaceStringCompare("abcdef###xyz", "abcw#xyz"))

# false
print(BackspaceStringCompare("abcdef###xyz", "abcdefxyz###"))