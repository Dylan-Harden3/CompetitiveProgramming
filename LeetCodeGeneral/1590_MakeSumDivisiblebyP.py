class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        goal = sum(nums) % p

        if goal == 0:
            return 0

        res = len(nums)
        pf_to_idx = {0: -1}
        cur = 0
        for i, n in enumerate(nums):
            cur = (cur + n) % p
            pf_to_idx[cur] = i

            if (cur - goal + p) % p in pf_to_idx:
                res = min(res, i - pf_to_idx[(cur - goal + p) % p])
    
        return res if res < len(nums) else -1
