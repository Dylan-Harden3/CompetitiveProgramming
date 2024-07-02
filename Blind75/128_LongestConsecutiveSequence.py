class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        bag = set(nums)

        ml = 0 if nums == [] else 1
        for n in bag:
            if n-1 not in bag:
                cur = n
                while cur + 1 in bag:
                    cur += 1
                    ml = max(ml, cur - n + 1)
        return ml