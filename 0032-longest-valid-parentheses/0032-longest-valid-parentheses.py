class Solution:
    def longestValidParentheses(self, s: str) -> int:
        answer_set = [0]
        max_answer = 0
        
        for i in range(len(s)):
            if s[i] == '(':
                answer_set.append(0)
            else:
                if len(answer_set) > 1:
                    a = answer_set.pop()
                    answer_set[-1] += a + 2
                    max_answer = max(max_answer, answer_set[-1])
                else:
                    answer_set = [0]
                
        return max_answer