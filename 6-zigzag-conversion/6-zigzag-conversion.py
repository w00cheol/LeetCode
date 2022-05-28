class Solution:
    def convert(self, s: str, numRows: int) -> str:
        answer = []
        if numRows == 1 or len(s)<=numRows: return s
        for i in range(numRows-1):
            cnt = 1
            j = i
            answer.append(s[j])
            while j < len(s):
                j = j+2*(numRows-1-i)
                if j >= len(s): break
                answer.append(s[j])
                if i !=0 and numRows>3:
                    j = j+2*i
                    if j >= len(s): break
                    answer.append(s[j])
                    
        for i in range(numRows-1, len(s), 2*(numRows-1)): answer.append(s[i])
        
        answer = "".join(answer)
        return answer