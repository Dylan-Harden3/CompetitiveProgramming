class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        h = defaultdict(int)
        l = res =0
        for r in range(len(nums)):
            h[nums[r]] += 1
            while h[nums[r]] > k and l <= r:
                h[nums[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
