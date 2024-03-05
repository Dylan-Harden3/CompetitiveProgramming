class Solution:
    def fib(self, n: int) -> int:
        secondLast = 0
        last = 1
        if n <= 1: return n

        for i in range(2, n+1):
            ith = secondLast + last
            secondLast = last
            last = ith
        return last
