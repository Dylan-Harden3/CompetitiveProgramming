class Solution:
    def customSortString(self, order: str, s: str) -> str:
        sCounts = Counter(s)

        res = []
        for c in order:
            if c in sCounts:
                res += [c] * sCounts[c]
                sCounts.pop(c)
        
        for c in sCounts:
            res += [c] * sCounts[c]

        return ''.join(res)