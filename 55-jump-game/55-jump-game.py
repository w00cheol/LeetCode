class Solution:
    def canJump(self, nums: List[int]) -> bool:
        M = 0
        for i in range(len(nums)):
            if i > M:
                return False
            M = max(M, i + nums[i])
            if M >= len(nums)-1:
                return True