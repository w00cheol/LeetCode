class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        for x in range(len(s)):
            test = [s[x]]
            while x<len(s)-1 and s[x+1] not in test:
                test.append(s[x+1])
                x = x+1
            answer = max(answer, len(test))
            
        return answer