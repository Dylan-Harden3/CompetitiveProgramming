class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        sums = defaultdict(int)
        sums[0] = 1
        res = 0
        for num in nums:
            total += num
            if total - k in sums:
                res += sums[total-k]
            sums[total] += 1
        return res
