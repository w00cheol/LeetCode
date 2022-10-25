class Solution:
    def totalNQueens(self, n):
        cols = set()
        pos_diag = set()
        neg_diag = set()
        
        def backTracking(row):
            count = 0
            if row == n:
                return 1
                
            for col in range(n):
                if col in cols or (row + col) in pos_diag or (row - col) in neg_diag:
                    continue
                
                cols.add(col)
                pos_diag.add(row + col)
                neg_diag.add(row - col)
                
                count += backTracking(row+1)
                
                cols.remove(col)
                pos_diag.remove(row + col)
                neg_diag.remove(row - col)
            
            return count
            
        return backTracking(0)