class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        tgt = sum(nums) // 2
        dp = set([0])

        for num in nums:
            cur = set()
            for s in dp:
                cur.add(s)
                cur.add(s + num)
                if s + num == tgt:
                    return True
            dp = cur
        return False
