class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for pos in range(len(s)):
            i = 0
            while pos-i >= 0 and pos+i <= len(s)-1:
                if s[pos-i] != s[pos+i]:
                    break
                res += 1
                i += 1
        
        for p1, p2 in zip(range(len(s)-1), range(1, len(s))):
            i = 0
            while p1-i >= 0 and p2+i <= len(s)-1:
                if s[p1-i] != s[p2+i]:
                    break
                res += 1
                i += 1
        
        return res
