class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur_sum = 0
        for i in range(k):
            cur_sum += nums[i]

        max_avg = cur_sum / k

        l = 0
        r = k

        while r < len(nums):
            cur_sum -= nums[l]
            cur_sum += nums[r]
            max_avg = max(max_avg, cur_sum / k)
            l += 1
            r += 1
        
        return max_avg
