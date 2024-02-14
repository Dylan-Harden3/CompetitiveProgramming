class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0]

        for n in nums:
            prefix.append(prefix[-1] + n)

        for i in range(1, len(nums)+1):
            if prefix[i-1] == prefix[-1] - prefix[i]:
                return i-1
        
        return -1
