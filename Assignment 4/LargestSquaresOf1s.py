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
                # If the current cell is 1, we can extend the square by considering the minimum value
                # of the left, upper, and upper-left cells and adding 1.
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

                # Update the maximum side length if the current cell can form a larger square.
                max_side = max(max_side, dp[i][j])

    # Return the area of the largest square (side length squared).
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