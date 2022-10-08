class Solution:
    def generateMatrix(self, n):
        answer = [[False] * n for _ in range(n)]
        x, y = 0, 0
        dx, dy = 1, 0
        
        for i in range(1, n*n + 1):
            answer[y][x] = i
            
            if x+dx == n or y+dy == n or answer[y+dy][x+dx]:
                dx, dy = -dy, dx
                
            x = x + dx
            y = y + dy
    
        return answer
    
    