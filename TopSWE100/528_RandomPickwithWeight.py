class Solution:

    def __init__(self, w: List[int]):
        s = 0
        self.pf = []
        for weight in w:
            s += weight
            self.pf.append(s)
        self.s = s

    def pickIndex(self) -> int:
        i = random.uniform(0, self.s)
        l, r = 0, len(self.pf)
        res = 0
        while l < r:
            m = (l+r)//2
            if self.pf[m] < i:
                l = m+1
            else:
                r = m
        return l

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()