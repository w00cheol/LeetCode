class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        answer = 2e9
        l, r, running_sum = 0, 0, 0
        
        while r < len(nums):
            running_sum += nums[r]
            r += 1
            
            while running_sum >= target:
                answer = min(answer, r - l)
                running_sum -= nums[l]
                l += 1
            
        return answer if answer != 2e9 else 0