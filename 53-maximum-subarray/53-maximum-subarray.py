class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        start = nums[0]
        answer = nums[0]
        for i in range(1, len(nums)):
            start = max(start+nums[i], nums[i])
            answer = max(answer, start)
        return answer