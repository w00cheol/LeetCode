class Solution:
    def permuteUnique(self, nums):
        def dfs(nums, answer, permutationList = []):
            if not nums:
                answer.add(tuple(permutationList))
                return
            
            for i in range(len(nums)):
                dfs(nums[:i] + nums[i+1:], answer, permutationList + [nums[i]])
            
        answer = set()
        dfs(nums, answer)
        return answer