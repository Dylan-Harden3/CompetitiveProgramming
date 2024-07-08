class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0

        for i in range(32):
            cur = n >> i
            res += (cur & 1)
        
        return res