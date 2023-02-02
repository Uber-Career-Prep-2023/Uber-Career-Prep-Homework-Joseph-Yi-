

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
