class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        subarr_sums = []
        MOD = 10**9 + 7

        for i in range(n):
            cur = 0
            for j in range(i, n):
                cur += nums[j]
                cur = cur % MOD
                subarr_sums.append(cur)

        subarr_sums.sort()

        res = 0
        for i in range(left-1, right):
            res += subarr_sums[i]
            res = res % MOD
        return res