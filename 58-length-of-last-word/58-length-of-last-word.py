class Solution:
    def lengthOfLastWord(self, s:str):
        answer = 0
        index = len(s) - 1
        
        while s[index] == ' ':
            index -= 1
        
        while index >= 0 and s[index] != ' ':
            answer += 1
            index -= 1
            
        return answer