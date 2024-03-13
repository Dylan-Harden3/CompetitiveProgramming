class Solution:
    def pivotInteger(self, n: int) -> int:
        pf = [0]

        for i in range(1, n+1):
            pf.append(pf[-1] + i)
        
        for i in range(1, n+1):
            if pf[i-1] == pf[-1] - pf[i]:
                return i
        return -1