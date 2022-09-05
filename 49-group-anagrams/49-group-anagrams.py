from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for str in strs:
            dic[('').join(sorted(str))].append(str)
        return dic.values()