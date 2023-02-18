class Solution:
    def minimumTotal(self, triangle):
        for r in range(1, len(triangle)):
            for c in range(len(triangle[r])):
                if c == 0:
                    triangle[r][c] += triangle[r - 1][0]
                    
                elif c == r:
                    triangle[r][c] += triangle[r - 1][-1]
                    
                else:
                    triangle[r][c] += min(triangle[r - 1][c - 1], triangle[r - 1][c])
                    
        return min(triangle[-1])