class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    if r+1-l > len(res):
                        res = s[l:r+1]
                    l -= 1
                    r += 1
                else:
                    break
        
        for i in range(1, len(s)):
            l, r = i-1, i
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    if r+1-l > len(res):
                        res = s[l:r+1]
                    l -= 1
                    r += 1
                else:
                    break
        return res
