class Solution:
    def climbStairs(self, n: int) -> int:

        two_ahead = 0
        one_ahead = 0
        cur = 1

        for i in range(n):
            x = cur + one_ahead
            two_ahead = one_ahead
            one_ahead = cur
            cur = x
        return cur
