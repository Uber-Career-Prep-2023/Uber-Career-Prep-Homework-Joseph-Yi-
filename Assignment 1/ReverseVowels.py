# Forward/backward two-pointer

# time complexity is O(n)
# the time is porportional to the length of the array because you search through
# the array once

# space complexity is O(n)
# beside the constant amount space required for the vowel set and the two 
# pointers, there must also be a list made that is the same length as s

#   approach
#   1. convert the string to a list
#   2. have a pointer at the beggining and the end of the list
#   3. keep moving the pointeres closer to the center
#       a. dont move the pointer if it has landed on a vowel
#   4. if both are vowels swap
#   5. stop when you've reached the middle

# this problem took me about 15 min

def ReverseVowels(s):

    vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
    s = list(s)

    left = 0
    right = len(s) - 1
    
    while left < right:
        if s[left] in vowels and s[right] in vowels:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            left += 1
            right -= 1
        elif s[left] in vowels:
            right -= 1
        elif s[right] in vowels:
            left += 1
        else:
            left += 1
            right -= 1
    return ''.join(s)



def main():
    print(ReverseVowels("Uber Career Prep"))
    print(ReverseVowels("xyz"))
    print(ReverseVowels("flamingo"))
    print(ReverseVowels("AeIOu"))


if __name__ == "__main__":
    main()
