class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        sols = set()
        for i in range(len(nums)-2):
            l, r = i+1, len(nums)-1
            while l < r:
                if nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    if (nums[i], nums[l], nums[r]) not in sols:
                        sols.add((nums[i], nums[l], nums[r]))
                    l += 1
        return sols