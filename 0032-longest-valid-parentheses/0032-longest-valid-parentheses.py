class Solution:
    def longestValidParentheses(self, s):
        answer = 0
        answer_group = [0]
        
        for i in range(len(s)):
            if s[i] == '(': # beginning of new group
                answer_group.append(0)
            elif len(answer_group) > 1: # which means there is '(' that is still unclosed
                
                # so we can remove one '(' to make one more group (length is 2)
                last_group = answer_group.pop() + 2
                
                # if there is no '(' between two group we can combine them
                answer_group[-1] += last_group
                
                # check new last group we have combine
                answer = max(answer, answer_group[-1])
            else:
                # ')' exists more so we have to restart
                answer_group = [0]
                
        return answer