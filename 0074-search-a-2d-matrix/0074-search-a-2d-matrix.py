class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, (len(matrix) * len(matrix[0]) - 1)
        
        while left <= right:
            mid = (left + right) // 2
            row, col = mid // len(matrix[0]), mid % len(matrix[0])
            
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1
            
        return False