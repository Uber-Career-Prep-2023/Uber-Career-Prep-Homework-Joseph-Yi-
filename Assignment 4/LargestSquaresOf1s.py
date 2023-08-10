# DP memorization

# Time complexity is O(n^2)
# you search every column and row of the matrix thus O(n^2)

# Space Complexity is O(n^2)
# the dp array is the same size as the matrix

# This function took me 31 min
def largestSquareOf1s(matrix):
    if not matrix:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])

    # Create a new matrix to store the dimensions of the largest square ending at each cell.
    dp = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]

    max_side = 0

    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            if matrix[i - 1][j - 1] == 1:
                
                # updates the new max to be the min of all adjacent sides
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

                max_side = max(max_side, dp[i][j])

    
    return max_side



matrix = [
    [1, 0, 1, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 1, 1, 1, 0],
    [1, 1, 1, 1, 1],
    [1, 1, 0, 0, 1]
]
print(largestSquareOf1s(matrix))


matrix = [
    [0, 1, 0, 1, 1],
    [0, 0, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 1, 1, 0, 0]
]
print(largestSquareOf1s(matrix))

matrix = [
    [0, 1, 0, 1],
    [0, 0, 1, 1],
    [0, 1, 1, 1],
    [0, 0, 1, 1]
]
print(largestSquareOf1s(matrix))