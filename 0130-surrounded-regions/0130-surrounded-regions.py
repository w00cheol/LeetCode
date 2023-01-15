class Solution:
    def solve(self, board: List[List[str]]) -> None:
        connected_with_border = set()
        
        def dfs(r, c):
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
                return
            if board[r][c] == 'X':
                return
            if (r, c) in connected_with_border:
                return
            
            connected_with_border.add((r, c))
            
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for r in range(len(board)):
            if board[r][0] == 'O':
                dfs(r, 0)
            if board[r][-1] == 'O':
                dfs(r, len(board[0]) - 1)
                
        for c in range(len(board[0])):
            if board[0][c] == 'O':
                dfs(0, c)
            if board[-1][c] == 'O':
                dfs(len(board) - 1, c)
            
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'O' and (r, c) not in connected_with_border:
                    board[r][c] = 'X'