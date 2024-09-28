class Solution:
    def minElement(self, nums: List[int]) -> int:
        
        def digitSum(num):
            res = 0
            pwr = 1
            while num >= pwr:
                if num == pwr:
                    return 1
                res += (num // pwr % 10)
                pwr *= 10
            return res
        res = inf
        for num in nums:
            res = min(res, digitSum(num))
        return res
