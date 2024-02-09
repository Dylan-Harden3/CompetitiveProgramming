class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = "123456789"
        res = []
        for i in range(len(str(low)), len(str(high))+1):
            l,r = 0, i
            while r < 10:
                num = int(digits[l:r])
                if num >= low and num <= high:
                    res.append(num)
                l += 1
                r += 1
        return res
