class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        s1set = set(s1)
        res = False
        for r in range(len(s2)):
            while (s2[l] not in s1set or (r-l+1)>len(s1)) and l < r:
                l += 1
            if Counter(s2[l:r+1]) == Counter(s1):
                return True
        return False
