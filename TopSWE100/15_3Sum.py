class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sols = set()
        for i, n in enumerate(nums):
            l, r = i+1, len(nums)-1
            while l < r:
                if n + nums[l] + nums[r] > 0:
                    r -= 1
                elif n + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    if (n, nums[l], nums[r]) not in sols:
                        sols.add((n, nums[l], nums[r]))
                    l += 1
                    r -= 1
        return sols
