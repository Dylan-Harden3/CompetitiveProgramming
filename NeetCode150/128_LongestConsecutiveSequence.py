class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = set(nums)
        res = 0
        candidates = []
        for num in nums:
            if num-1 not in n:
                candidates.append(num)

        for c in candidates:
            x = c
            while x + 1 in n:
                x += 1
            res = max(res, x-c+1)

        return res
