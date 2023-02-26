class Solution:
    def searchMatrix(self, matrix, target):
        r, c = 0, len(matrix[0]) - 1
        
        while r < len(matrix) and c >= 0:
            if target == matrix[r][c]:
                return True

            elif target < matrix[r][c]:
                c -= 1
                
            elif target > matrix[r][c]:
                r += 1
            
        return False