class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        neg = False
        if x < 0:
            neg = True
        elif x == 0:
            return 0

        x = abs(x)
                
        digits = []
        while x > 0:
            digits.append(x % 10)
            x = x // 10
        
        digits = digits[::-1]
        res = 0
        for i, digit in enumerate(digits):
            if INT_MAX - res <= ((10**i) * digit):
                return 0
            res += (10**i) * digit

        return -res if neg else res
