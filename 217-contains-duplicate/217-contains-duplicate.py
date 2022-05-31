from collections import defaultdict

class Solution:
    def containsDuplicate(self, nums: List[int]):
        dic = defaultdict(int)
        for i in nums:
            if dic[i] == 1:
                return True
            dic[i] += 1
        return False