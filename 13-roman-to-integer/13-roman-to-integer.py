class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ''
        mini = min(strs, key=lambda x:len(x))
        lenA = len(mini)
        while lenA:
            if all(mini[:lenA] == st[:lenA] for st in strs):
                return str(mini[:lenA])
            lenA -= 1
        return answer