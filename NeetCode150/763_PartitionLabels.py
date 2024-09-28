class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        l, r = 0, 0
        max_pos = defaultdict(int)

        for i, c in enumerate(s):
            max_pos[c] = max(max_pos[c], i)
        
        for i, c in enumerate(s):
            r = max(r, max_pos[c])
            if r == i:
                res.append(r-l+1)
                r += 1
                l = r
        return res
