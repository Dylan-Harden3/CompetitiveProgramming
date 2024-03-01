class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        res = 0
        for i in range(32):
            if (c >> i) & 1:
                res += 1 if ((a >> i) & 1) == 0 and ((b >> i) & 1) == 0 else 0
            else:
                res += (a >> i & 1)
                res += (b >> i & 1)
        return res
