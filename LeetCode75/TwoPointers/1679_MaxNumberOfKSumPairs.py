class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        c = Counter(nums)
        res = 0 

        for n in c:
            temp = k - n

            if temp == n:
                res += c[n] // 2
            elif n < temp:
                res += min(c[n], c[temp])
    
        return res
