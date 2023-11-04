
#
# Complete the 'numCells' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY grid as parameter.
#

def is_dominant_cell(grid, n, m):
    # Write your code here
    value = grid[n][m]
    neighbors = [(n -1,m -1),(n-1,m),(n-1,m+1),(n,m-1),(n,m+1),(n+1,m-1),(n+1,m),(n+1,m+1)]
    for neighbor_row,neighbor_col in neighbors:
        if 0 <= neighbor_row < len(grid) and 0 <= neighbor_col < len(grid[0]) and grid[neighbor_row][neighbor_col] >= value:
            return False
    return True
def numCells(grid):
    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if is_dominant_cell(grid,row,col):
                count += 1
    return count
    
    
    