class Solution:
    def subsetsWithDup(self, nums):
        def dfs(idx, curr):
            answers.append(curr)
            
            for i in range(idx, len(nums)):
                if i == idx or nums[i] != nums[i- 1]:
                    dfs(i + 1, curr + [nums[i]])
                    
        answers = []
        nums.sort()
        
        dfs(0, [])
        return answers