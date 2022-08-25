class Solution:
    def isValidSudoku(self, board: List[List[str]]):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    continue
                
                if board[i][j] not in rows[i]:
                    rows[i].add(board[i][j])
                else:
                    return False
                
                if board[i][j] not in cols[j]:
                    cols[j].add(board[i][j])
                else:
                    return False
                
                b = (i//3) * 3 + (j//3)
                if board[i][j] not in boxes[b]:
                    boxes[b].add(board[i][j])
                else:
                    return False
                
        return True