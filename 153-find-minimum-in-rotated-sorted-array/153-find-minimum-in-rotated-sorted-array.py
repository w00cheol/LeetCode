class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        mid = (left + right)//2
        M = m = nums[0]
        
        while left <= right:
            m = min(m, nums[mid])
            if nums[mid] >= M:
                M = nums[mid]
                left = mid + 1
                mid = (left+right)//2
            else:
                right = mid - 1
                mid = (left+right)//2
        return m