class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums)-1
        
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
            
        if i == 0:
            nums[::] = nums[::-1]
            return
        
        min_bigger = i-1
        for k in range(i, len(nums)):
            if nums[k] > nums[i-1]:
                min_bigger = k
                       
        nums[i-1], nums[min_bigger] = nums[min_bigger], nums[i-1]
        
        nums[::] = nums[:i] + nums[i:][::-1]
        return