class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = defaultdict(int)
        curSum = 0
        sums[0] = 1
        res = 0
        for num in nums:
            curSum += num
            if curSum-k in sums:
                res += sums[curSum-k]
            sums[curSum] += 1
        return res