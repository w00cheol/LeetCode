class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3: return max(nums)
        rob_first = nums[2:len(nums)-1]
        rob_not_first = nums[1:]
        if len(rob_first) == 1:
            rob_first[0] += nums[0]
        else:
            rob_first[0] += nums[0]
            rob_first[1] += nums[0]
            rob_first[1] = max(rob_first[0], rob_first[1])
        rob_not_first[1] = max(rob_not_first[0], rob_not_first[1])
        for i in range(2, len(rob_first)):
            rob_first[i] = max(rob_first[i-1], rob_first[i-2] + rob_first[i])
        for i in range(2, len(rob_not_first)):
            rob_not_first[i] = max(rob_not_first[i-1], rob_not_first[i-2] + rob_not_first[i])
        return max(rob_first[-1], rob_not_first[-1])