class Solution:
    def setZeroes(self, matrix):
        dic = {'row': False, 'col': False}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
                    if i == 0: dic['row'] = True
                    if j == 0: dic['col'] = True
        for i in range(1, len(matrix[0])):
            if matrix[0][i] == 0:
                for j in range(1, len(matrix)):
                    if matrix[j][i] != 0: matrix[j][i] = '#'
        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                for j in range(1, len(matrix[0])):
                    matrix[i][j] = 0
                continue
            for j in range(len(matrix[0])):
                if matrix[i][j] == '#': matrix[i][j] = 0
        if dic['row']:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
        if dic['col']:
            for i in range(len(matrix)):
                matrix[i][0] = 0