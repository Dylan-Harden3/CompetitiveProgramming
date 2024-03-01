class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            num_ones = 0
            for j in range(32):
                if i >> j & 1:
                    num_ones += 1
            ans.append(num_ones)
        return ans
