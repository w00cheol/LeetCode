class Solution:
    def exist(self, board, word):
        def find(board, i, j, word):
            if board[i][j] == word[0]:
                if len(word) == 1:
                    return True
                value = board[i][j]
                board[i][j] = None
                if i+1 < len(board) and find(board, i+1, j, word[1:]): return True
                if j+1 < len(board[0]) and find(board, i, j+1, word[1:]): return True
                if i-1 >= 0 and find(board, i-1, j, word[1:]): return True
                if j-1 >= 0 and find(board, i, j-1, word[1:]): return True
                board[i][j] = value
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if find(board, i, j, word): return True
        return False