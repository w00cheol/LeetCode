class Solution:
    def solveNQueens(self, n: int):
        board = [['.' for _ in range(n)] for _ in range(n)]
        answer = []
        
        def backTracking(row):
            if isValid(board) == False:
                return
            if row == n:
                answer.append([''.join(board[i]) for i in range(n)])
                return
            
            for i in range(len(board[0])):
                board[row][i] = 'Q'
                backTracking(row + 1)
                board[row][i] = '.'
            
            return
        
        def isValid(board):
            l_upper_diag = set()
            r_upper_diag = set()
            
            for c in range(len(board[0])):
                col_has_queen = False
                for r in range(len(board)):
                    if board[r][c] == 'Q':
                        if col_has_queen or (r-c) in l_upper_diag or (r+c) in r_upper_diag:
                            return False
                        else:
                            col_has_queen = True
                            l_upper_diag.add(r-c)
                            r_upper_diag.add(r+c)
            return True
        
        backTracking(0)
        return answer
        
        
