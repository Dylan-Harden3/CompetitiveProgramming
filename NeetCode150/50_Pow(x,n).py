class Solution:
    def myPow(self, x: float, n: int) -> float:
        neg = False
        if n == 0:
            return 1
        elif n < 0:
            neg = True
            n = abs(n)
        
        powers = [(1, x)]
        power = 1
        res = x
        while power*2 <= n:
            power *= 2
            res *= res
            powers.append((power, res))

        needed = n - power
        for i in range(len(powers)-1, -1, -1):
            if powers[i][0] <= needed:
                needed -= powers[i][0]
                res *= powers[i][1]
        
        return 1/res if neg else res
