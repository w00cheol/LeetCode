class Solution:
    def solveNQueens(self, n):
        board = [['.' for _ in range(n)] for _ in range(n)]
        columns = set()
        l_upper_diag = set()
        r_upper_diag = set()
        answer = []
        
        def backTracking(row):
            if row == n:
                answer.append([''.join(board[i]) for i in range(n)])
                return
            
            for col in range(len(board[0])):
                if col in columns or (row-col) in l_upper_diag or (row+col) in r_upper_diag:
                    continue
                    
                columns.add(col)
                l_upper_diag.add(row-col)
                r_upper_diag.add(row+col)
                board[row][col] = 'Q'
                
                backTracking(row+1)
                
                columns.remove(col)
                l_upper_diag.remove(row-col)
                r_upper_diag.remove(row+col)
                board[row][col] = '.'
            
            return
        
        backTracking(0)
        return answer
        
        
