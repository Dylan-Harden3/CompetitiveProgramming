class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        counts = defaultdict(int)
        max_occs = 0
        
        for r in range(len(s)):
            counts[s[r]] += 1
            max_occs = max(max_occs, counts[s[r]])
            while (r-l+1) - max_occs > k:
                counts[s[l]] -= 1
                if counts[s[l]] == 0:
                    counts.pop(s[l])
                l += 1
            res = max(res, r-l+1)
        return res
