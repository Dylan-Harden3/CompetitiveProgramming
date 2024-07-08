class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            cur = (n >> i) & 1
            res = res >> (31-i)
            if cur:
                res = res | cur
            res = res << (31-i)
        return res
