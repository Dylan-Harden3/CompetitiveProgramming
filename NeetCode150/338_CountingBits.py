class Solution:
    def countBits(self, n: int) -> List[int]:
        def numOnes(n):
            res = 0
            for i in range(32):
                res += (n >> i) & 1
            return res
        return [numOnes(i) for i in range(n+1)]
