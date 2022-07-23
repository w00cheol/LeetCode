class Solution:
    def spiralOrder(self, matrix):
        x, y = 0, 0
        answer = [matrix[x][y]]
        matrix[x][y] = None
        while len(answer) != len(matrix)*len(matrix[0]):
            while y+1 < len(matrix[0]) and matrix[x][y+1] != None:
                    y += 1
                    answer.append(matrix[x][y])
                    matrix[x][y] = None
            while x+1 < len(matrix) and matrix[x+1][y] != None:
                    x += 1
                    answer.append(matrix[x][y])
                    matrix[x][y] = None
            while y-1 >= 0 and matrix[x][y-1] != None:
                    y -= 1
                    answer.append(matrix[x][y])
                    matrix[x][y] = None
            while x-1 >= 0 and matrix[x-1][y] != None:
                    x -= 1
                    answer.append(matrix[x][y])
                    matrix[x][y] = None
        return answer