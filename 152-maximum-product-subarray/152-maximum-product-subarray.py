class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxnow = minnow = answer = nums[0]
        for i in range(1, len(nums)):
            if nums[i] >= 0:
                maxnow = max(maxnow*nums[i], nums[i])
                minnow = min(minnow*nums[i], nums[i])
            else:
                temp = maxnow
                maxnow = max(minnow*nums[i], nums[i])
                minnow = min(temp*nums[i], nums[i])
            answer = max(answer, maxnow)
        return answer