class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for c in range(1, len(grid[0])):
            grid[0][c] += grid[0][c - 1]
            
        for r in range(1, len(grid)):
            grid[r][0] += grid[r - 1][0]
            
        for r in range(1, len(grid)):
            for c in range(1, len(grid[0])):
                grid[r][c] += min(grid[r][c - 1], grid[r - 1][c])
                
        return grid[-1][-1]