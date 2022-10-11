class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLeft(nums, target):
            l, r = 0, len(nums) - 1

            while l <= r:
                mid = (l+r) // 2
                
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] >= target:
                    r = mid - 1
                    
            return l
            
        def findRight(nums, target):
            l, r = 0, len(nums) - 1
            
            while l <= r:
                mid = (l+r) // 2
                
                if nums[mid] > target:
                    r = mid - 1
                elif nums[mid] <= target:
                    l = mid + 1
                
            return r
        
        left = findLeft(nums, target)
        right = findRight(nums, target)
        
        return [left, right] if left <= right else [-1, -1]