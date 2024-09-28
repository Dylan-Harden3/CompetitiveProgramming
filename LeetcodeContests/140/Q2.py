class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        maximumHeight.sort(reverse=True)
        n = len(maximumHeight)
        res = 0
        minH = inf
        for i in range(n):
            if maximumHeight[i] < minH:
                minH = maximumHeight[i]
            else:
                minH -= 1
            res += minH
            if minH < 0:
                return -1
        return res
