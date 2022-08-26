class Solution:
    def lengthOfLastWord(self, s):
        answer = 0
        index = len(s) - 1
        
        while s[index] == ' ':
            index -= 1
        
        while s[index] != ' ':
            answer += 1
            index -= 1
            if index < 0:
                break
            
        return answer