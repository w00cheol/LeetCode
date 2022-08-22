class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        answer = []
        dic = {
                '2':"abc", '3':"def", '4':"ghi", '5':"jkl",
                '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"
        }
        
        if len(digits) == 0: return None
        
        def dfs(i, string):
            if i == len(digits):
                answer.append(string)
            else:
                alphabets = dic[digits[i]]
                for alphabet in alphabets:
                    dfs(i+1, string + alphabet)

        dfs(0, "")
        return answer