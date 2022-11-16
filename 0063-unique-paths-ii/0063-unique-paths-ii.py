class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        if obstacleGrid[0][0] or obstacleGrid[-1][-1]:
            return 0
        
        for row in range(len(obstacleGrid)):
            for col in range(len(obstacleGrid[0])):
                if obstacleGrid[row][col] == 1:
                    obstacleGrid[row][col] = -1
                    
        obstacleGrid[0][0] = 1
        
        for row in range(1, len(obstacleGrid)):
                if obstacleGrid[row][0] == 0 and obstacleGrid[row - 1][0] != -1:
                    obstacleGrid[row][0] = 1
                else:
                    obstacleGrid[row][0] = -1
                    
        for col in range(1, len(obstacleGrid[0])):
                if obstacleGrid[0][col] == 0 and obstacleGrid[0][col-1] != -1:
                    obstacleGrid[0][col] = 1
                else:
                    obstacleGrid[0][col] = -1

        for row in range(1, len(obstacleGrid)):
            for col in range(1, len(obstacleGrid[0])):
                if obstacleGrid[row][col] != -1:
                    obstacleGrid[row][col] = max(0, obstacleGrid[row-1][col]) + max(0, obstacleGrid[row][col-1])
                    
        return obstacleGrid[-1][-1]