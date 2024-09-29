class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()

        def sos(n):
            res = 0
            while n:
                res += (n % 10)**2
                n = n // 10
            return res

        while n != 1:
            if n in visit:
                return False
            visit.add(n)
            n = sos(n)
            
        return True
