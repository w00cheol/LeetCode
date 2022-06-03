class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if target == nums[left]:
                return left
            if target == nums[right]:
                return right
            if target == nums[mid]:
                return mid
            if nums[left] < nums[mid]:
                if target < nums[mid] and target > nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target < nums[right] and target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1