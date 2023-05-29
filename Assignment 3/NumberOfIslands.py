# Space Complexity is O(1)
# the only additional space that is need 

# Time complexity is O(n * m) where n is number of rows and m is number of columns

def numIslands(grid):
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
        grid[row][col] = '#'
        
        dfs(row + 1, col)  # Check down
        dfs(row - 1, col)  # Check up
        dfs(row, col + 1)  # Check right
        dfs(row, col - 1)  # Check left