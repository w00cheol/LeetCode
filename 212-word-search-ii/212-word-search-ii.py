class Solution:
    def findWords(self, board, words):
        def insert(word, trie):
            for w in word:
                if w not in trie: trie[w] = {}
                trie = trie[w]
            trie['#'] = True
            
        def filter_possibilities(i, j, board, dictionary, possibility):
            if not board[i][j]: return
            c = board[i][j]
            board[i][j] = None
            if c in dictionary:
                p = possibility+c
                if '#' in dictionary[c]:
                    answer.append(p)
                    del dictionary[c]['#']
                if i-1 >= 0:
                    filter_possibilities(i-1, j, board, dictionary[c], p)
                if i+1 <= len(board)-1:
                    filter_possibilities(i+1, j, board, dictionary[c], p)
                if j-1 >= 0:
                    filter_possibilities(i, j-1, board, dictionary[c], p)
                if j+1 <= len(board[0])-1:
                    filter_possibilities(i, j+1, board, dictionary[c], p)
            board[i][j] = c
            return
                    
        dictionary, answer = {}, []
        for word in words:
            insert(word, dictionary)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in dictionary:
                    filter_possibilities(i, j, board, dictionary, '')
        return answer