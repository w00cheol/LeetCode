class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        
        def dfs(nums):
            if nums in answer:
                return
            answer.append(nums)
            for i in range(len(nums)):
                dfs(nums[:i] + nums[i+1:])
        
        dfs(nums)
        return answer