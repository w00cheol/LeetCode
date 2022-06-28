class Solution:
    def dfs(self, grid, i, j):
        grid[i][j] = 0
        if i > 0 and grid[i-1][j] == '1':
            self.dfs(grid, i-1, j)
        if i < len(grid) - 1 and grid[i+1][j] == '1':
            self.dfs(grid, i+1, j)
        if j > 0 and grid[i][j-1] == '1':
            self.dfs(grid, i, j-1)
        if j < len(grid[0]) - 1 and grid[i][j+1] == '1':
            self.dfs(grid, i, j+1)
            
    def numIslands(self, grid: List[List[str]]) -> int:
        answer = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    answer += 1
        return answer