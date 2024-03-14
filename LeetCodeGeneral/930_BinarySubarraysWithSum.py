class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        def helper(goal):
            if goal < 0: return 0
            res = 0
            l, curSum = 0, 0
            for r in range(len(nums)):
                curSum += nums[r]
                while curSum > goal:
                    curSum -= nums[l]
                    l += 1
                res += r-l + 1

            return res

        return helper(goal) - helper(goal-1)