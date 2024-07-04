class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        bag = set()
        res = 0
        l = 0

        for r in range(len(s)):
            while l < r and s[r] in bag:
                bag.remove(s[l])
                l += 1
            bag.add(s[r])
            res = max(res, r-l+1)
        return res