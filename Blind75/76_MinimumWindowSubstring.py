class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counts_t = Counter(t)
        satisfied_chars = set()
        counts_s = defaultdict(int)
        l = 0
        res, minl = '', inf

        for r in range(len(s)):
            if s[r] in t:
                counts_s[s[r]] += 1
                if counts_s[s[r]] >= counts_t[s[r]]:
                    satisfied_chars.add(s[r])
                
            while len(satisfied_chars) == len(counts_t.keys()):
                if minl > r-l+1:
                    minl = r-l+1
                    res = s[l:r+1]

                if s[l] in t:
                    counts_s[s[l]] -= 1
                    if counts_s[s[l]] < counts_t[s[l]]:
                        satisfied_chars.remove(s[l])
                l += 1
            
        return res