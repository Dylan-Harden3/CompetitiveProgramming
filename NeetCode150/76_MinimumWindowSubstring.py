class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = Counter(t)
        res, ml = '', inf
        satisfied_chars = set()
        goal = len(count_t)
        counts = defaultdict(int)
        l=0
        for r in range(len(s)):
            counts[s[r]] += 1
            if counts[s[r]] >= count_t[s[r]] and s[r] in count_t:
                satisfied_chars.add(s[r])
            
            while len(satisfied_chars) == goal and l < len(s):
                if (r-l+1) < ml:
                    res = s[l:r+1]
                    ml = r-l+1
                
                counts[s[l]] -= 1
                if counts[s[l]] < count_t[s[l]] and s[l] in satisfied_chars:
                    satisfied_chars.remove(s[l])
                l += 1
        return res
