

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