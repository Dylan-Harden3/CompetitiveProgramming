class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []

        def nOnes(n):
            res = 0
            for i in range(32):
                res += (n >> i) & 1
            return res

        for i in range(n+1):
            ans.append(nOnes(i))
        return ans