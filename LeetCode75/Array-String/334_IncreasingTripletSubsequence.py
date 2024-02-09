class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        n1, n2 = inf, inf

        for num in nums:

            if num < n1:
                n1 = num

            if num > n1 and num < n2:
                n2 = num

            if num > n1 and num > n2:
                return True
        return False
