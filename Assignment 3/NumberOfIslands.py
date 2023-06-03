# graph - DFS

# Space Complexity is O(1)
# the only additional space that is needed are the varibales 
# storing the rows length and count, all of which would be constant
# independent of the size of the matrix. 

# Time complexity is O(n * m) where n is number of rows and m is number of columns
# this function performs a DFS, which in the worst case will evaluate every single 
# entry in the matrix, thus resulting in the time being dependent on the 
# total size of the matrix

# Approach
# the function iterates through the matrix. Whenever the loop hits a 
# island, it performs a dfs, marking all adjacent island spaces with a
# 'x'. This increments the count. This continues until the every location
# in the array is visited. 

# This problem took me 7 min

def numberOfIslands(grid):
    if not grid:
        return 0
    
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    
    
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                count += 1
                dfs(row, col)
    
    return count


def dfs(row, col):
        # checks in bounds
        if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] != 1:
            return
        
        # marks the adjacent values
        grid[row][col] = 'x'
        
        dfs(row + 1, col)  # Check down
        dfs(row - 1, col)  # Check up
        dfs(row, col + 1)  # Check right
        dfs(row, col - 1)  # Check left