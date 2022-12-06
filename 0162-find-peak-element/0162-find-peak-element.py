class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # we don't know haw many peaks in this array
        # but 100% SURE num keeps increasing at least one time (because the first num is INF !)
        # and it is supposed to be decrease at least one time (because the last num is -INF !)
        
        # so find the index and that will be an answer
        l, r = 0, len(nums) - 1
        mid = 0
        
        while l < r:
            mid = (l + r) // 2
            
            if nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                r = mid
                
        return l