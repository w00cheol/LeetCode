class Solution:
    def minDistance(self, word1, word2) -> int:
        answer = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]

        for i in range(len(word1) + 1):
            answer[i][0] = i

        for i in range(len(word2) + 1):
            answer[0][i] = i

        for row in range(1, len(word1) + 1):
            for col in range(1, len(word2) + 1):
                answer[row][col] = min(answer[row-1][col] + 1, answer[row][col-1] + 1, answer[row-1][col-1] + (word1[row-1] != word2[col-1]))

        return answer[-1][-1]