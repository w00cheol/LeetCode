class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        if obstacleGrid[0][0] or obstacleGrid[-1][-1]:
            return 0
        
        for r in range(rows):
            for c in range(cols):
                if obstacleGrid[r][c] == 1:
                    obstacleGrid[r][c] = -1
                    
        obstacleGrid[0][0] = 1
        
        for r in range(1, rows):
                if obstacleGrid[r][0] == 0 and obstacleGrid[r - 1][0] != -1:
                    obstacleGrid[r][0] = 1
                else:
                    obstacleGrid[r][0] = -1
                    
        for c in range(1, cols):
                if obstacleGrid[0][c] == 0 and obstacleGrid[0][c-1] != -1:
                    obstacleGrid[0][c] = 1
                else:
                    obstacleGrid[0][c] = -1

        for r in range(1, rows):
            for c in range(1, cols):
                if obstacleGrid[r][c] != -1:
                    obstacleGrid[r][c] = max(0, obstacleGrid[r-1][c]) + max(0, obstacleGrid[r][c-1])
                    
        return obstacleGrid[-1][-1]