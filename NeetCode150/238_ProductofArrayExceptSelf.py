class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        right = [1]

        for num in nums:
            left.append(left[-1] * num)

        for num in nums[::-1]:
            right.append(right[-1] * num)
        right = right[::-1]
        
        res = [0] * len(nums)
        for i in range(len(nums)):
            res[i] = left[i] * right[i+1]
        return res
