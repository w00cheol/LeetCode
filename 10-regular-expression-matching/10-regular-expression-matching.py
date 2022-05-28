class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.BT(0, 0, s, p)
    
    def BT(self, s_index:int, p_index:int, s:str, p:str) -> bool:
        if p_index+1<len(p) and p[p_index+1] == '*':
            if self.BT(s_index, p_index+2, s, p): return 1
        if s_index == len(s):
            if p_index == len(p): return 1
            if p[p_index] == '*':
                if self.BT(s_index, p_index+1, s, p): return 1
            return 0
        elif p_index == len(p): return 0
        if s[s_index] == p[p_index] or p[p_index] == '.':
            if self.BT(s_index+1, p_index+1, s, p): return 1
        if p[p_index] == '*':
            if p[p_index-1] == '.':
                for i in range(s_index, len(s)):
                    if self.BT(i+1, p_index+1, s, p): return 1
            if self.BT(s_index, p_index+1, s, p): return 1
            preceding_check = s_index
            while preceding_check<len(s) and s[preceding_check] == p[p_index-1]:
                if self.BT(preceding_check+1, p_index+1, s, p): return 1
                preceding_check = preceding_check + 1
        return 0
    