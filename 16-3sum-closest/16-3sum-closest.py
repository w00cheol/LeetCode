class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        answer = nums[0] + nums[1] + nums[2]
        for left in range(len(nums)-2):
            mid = left + 1
            right = len(nums)-1
            while mid < right:
                temp = nums[left] + nums[mid] + nums[right]
                if temp == target:
                    return temp
                if abs(temp - target) < abs(answer - target):
                    answer = temp
                if temp < target:
                    mid += 1
                else:
                    right -= 1
        return answer