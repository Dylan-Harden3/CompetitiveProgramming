class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        trips = set()
        for i in range(len(nums)-2):
            tgt = -nums[i]
            l, r = i+1, len(nums)-1
            while l < r:
                if nums[l] + nums[r] < tgt:
                    l += 1
                elif nums[l] + nums[r] > tgt:
                    r -= 1
                else:
                    if (nums[i], nums[l], nums[r]) not in trips:
                        trips.add((nums[i], nums[l], nums[r]))
                    l += 1
        return list(trips)
