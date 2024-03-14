class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_counts = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while l < r and s[r] in char_counts:
                char_counts.remove(s[l])
                l += 1
            char_counts.add(s[r])
            res = max(res, r-l+1)
        return res