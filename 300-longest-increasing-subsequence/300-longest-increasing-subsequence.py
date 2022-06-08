class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > dp[-1]:
                dp.append(nums[i])
            elif nums[i] < dp[-1]:
                mid, l, r, temp = 0, 0, len(dp)-1, len(dp)-1
                while l <= r:
                    mid = (l+r)//2
                    if nums[i] < dp[mid]:
                        temp = mid
                        r = mid - 1
                    elif nums[i] == dp[mid]:
                        temp = mid
                        l = r + 1
                    else:
                        l = mid + 1
                dp[temp] = nums[i]
        return len(dp)