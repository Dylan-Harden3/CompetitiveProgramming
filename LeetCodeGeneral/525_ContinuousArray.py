class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        cache = {0: -1} # diff -> index
        zeros, ones = 0, 0
        res = 0
        for i, num in enumerate(nums):
            if num == 0:
                zeros += 1
            else:
                ones += 1
            
            diff = ones - zeros
            if diff in cache:
                res = max(res, i - cache[diff])
            else:
                cache[diff] = i
        return res
