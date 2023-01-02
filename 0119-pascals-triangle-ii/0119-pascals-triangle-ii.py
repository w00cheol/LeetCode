class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        answer = [1 for _ in range(rowIndex + 1)]
        
        for row in range(1, rowIndex + 1):
            for i in range((row // 2), 0, -1):
                answer[i] = answer[i - 1] + answer[i]
                
            if row % 2 == 1:
                answer[(row // 2) + 1] = answer[row // 2]

        if rowIndex % 2 == 1:
            return answer[:(rowIndex // 2) + 1] + answer[rowIndex // 2::-1]
        else:
            return answer[:rowIndex // 2] + answer[rowIndex // 2::-1]