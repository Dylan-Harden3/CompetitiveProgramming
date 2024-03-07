class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            m = (l+r)//2

            if (m == 0 or (m != 0 and nums[m-1] < nums[m])) and (m == len(nums)-1 or (m != len(nums)-1 and nums[m+1] < nums[m])):
                return m

            if nums[m] < nums[m+1]:
                l = m+1
            else:
                r = m-1
