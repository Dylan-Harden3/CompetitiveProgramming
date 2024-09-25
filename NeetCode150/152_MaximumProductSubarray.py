class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minProd = nums[0]
        maxProd = nums[0]
        res = nums[0]

        for num in nums[1:]:
            temp = maxProd
            maxProd = max(minProd * num, maxProd * num, num)
            minProd = min(minProd * num, temp * num, num)
            res = max(maxProd, res)
        
        return res
