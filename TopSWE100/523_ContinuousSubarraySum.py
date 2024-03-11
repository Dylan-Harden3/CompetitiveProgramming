class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        sums = {0: -1}
        curSum = 0

        for i, num in enumerate(nums):
            curSum += num
            curSum %= k
            if curSum not in sums:
                sums[curSum] = i
            elif i - sums[curSum] > 1:
                return True
        return False