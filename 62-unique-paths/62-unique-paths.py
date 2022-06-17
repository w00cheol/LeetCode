class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        answer = []
        grid = [[1 for _ in range(m)] for _ in range(n)]
        for i in range(m*n):
            x = i // m
            y = i % m
            if x and y:
                grid[x][y] = grid[x-1][y] + grid[x][y-1]
        return grid[-1][-1]