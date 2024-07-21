class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(l, r):
            res= ""
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    res = s[l:r+1]
                    l -= 1
                    r += 1
                else:
                    break
            return res
        
        res = ""
        for i in range(len(s)):
            cur = helper(i,i)
            if len(cur) > len(res):
                res = cur
        
        for i in range(len(s)-1):
            cur = helper(i,i+1)
            if len(cur) > len(res):
                res = cur
        
        return res