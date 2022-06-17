class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[1 for _ in range(m)] for _ in range(n)]
        for i in range(m*n):
            x, y = i // m, i % m
            if x and y:
                grid[x][y] = grid[x-1][y] + grid[x][y-1]
        return grid[-1][-1]