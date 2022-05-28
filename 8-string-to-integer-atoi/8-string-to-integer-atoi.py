class Solution:
    def myAtoi(self, s: str) -> int:
        answer = []
        i, sign = 0, 1
        while i < len(s):
            if s[i]>='0' and s[i] <= '9':
                answer.append(s[i])
                break
            elif s[i] == '-':
                sign = -1
                break
            elif s[i] == '+': break
            elif s[i] != ' ': return 0
            i = i+1
        i = i+1
        while i < len(s) and s[i]>='0' and s[i]<='9':
            answer.append(s[i])
            i = i+1
        if len(answer) == 0: return 0
        answer = int(''.join(answer))*sign
        if answer > 2**31-1: return 2**31-1
        elif answer < -2**31: return -2**31
        return answer