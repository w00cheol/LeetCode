class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = [[1]]
        
        for r in range(1, numRows):
            row = [0 for _ in range(r + 1)]
            
            row[0] = 1
            row[-1] = 1

            for c in range(1, r):
                row[c] = answer[r - 1][c - 1] + answer[r - 1][c]
                
            answer.append(row)
        
        return answer