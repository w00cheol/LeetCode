class Solution:
    def totalNQueens(self, n):
        global answer
        cols = set()
        pos_diag = set()
        neg_diag = set()
        answer = 0
        
        def backTracking(row):
            if row == n:
                global answer
                answer += 1
            
            for col in range(n):
                if col in cols or (row + col) in pos_diag or (row - col) in neg_diag:
                    continue
                
                cols.add(col)
                pos_diag.add(row + col)
                neg_diag.add(row - col)
                
                backTracking(row + 1)
                
                cols.remove(col)
                pos_diag.remove(row + col)
                neg_diag.remove(row - col)
            
        backTracking(0)
        return answer