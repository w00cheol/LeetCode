class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'(':')', '[':']', '{':'}'}
        answer = []
        for i in range(len(s)):
            if s[i] in dic:
                answer.append(dic[s[i]])
            else:
                if len(answer) == 0 or s[i] != answer.pop(): return False
        return len(answer) == 0
        