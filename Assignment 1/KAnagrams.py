def KAnagrams(s1, s2, k):

    if len(s1) != len(s2):
        return False

    char_count = [0] * 26
    for char in s1:
        char_count[ord(char) - ord('a')] += 1

    diff_count = 0
    for char in s2:
        idx = ord(char) - ord('a')
        char_count[idx] -= 1
        if char_count[idx] < 0:
            diff_count += 1
        if diff_count > k:
            return False

    return True

    