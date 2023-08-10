# DP Memorization

# Time comeplxity is O(n^2)
# The inner outer loop runs n times with the inner loop running upwards of n times
# resulting in a time complexity of n^2

# Space complexity is O(n)
# because you store n number of catalan numbers in the array.

# This took 8 min because I know the Catalan sequence
def generate_catalan_numbers(n):
    catalan_numbers = [0] * (n + 1)
    catalan_numbers[0] = 1

    for i in range(1, n + 1):
        for j in range(i):
            catalan_numbers[i] += catalan_numbers[j] * catalan_numbers[i - j - 1]

    return catalan_numbers

# Test examples
print(generate_catalan_numbers(1))  # Output: [1, 1]
print(generate_catalan_numbers(5))  # Output: [1, 1, 2, 5, 14, 42]
