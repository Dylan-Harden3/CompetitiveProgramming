class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if s == '': return 0
        res = 0
        counts = defaultdict(int)
        max_char = 0

        l = 0
        for r in range(len(s)):
            counts[s[r]] += 1
            max_char = max(max_char, counts[s[r]])

            if (r-l+1-max_char > k):
                counts[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        
        return res