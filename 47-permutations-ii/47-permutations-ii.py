class Solution:
    def permuteUnique(self, nums):
        answer = set()
        
        def dfs(nums, permutationList = []):
            if not nums:
                answer.add(tuple(permutationList))
                return
            
            for i in range(len(nums)):
                dfs(nums[:i] + nums[i+1:], permutationList + [nums[i]])
                
        dfs(nums)
        return answer