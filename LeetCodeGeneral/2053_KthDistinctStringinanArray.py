class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        c = Counter(arr)

        for el in arr:
            if c[el] == 1:
                c[el] -= 1
            if c[el] == 0:
                k -= 1
            if k == 0:
                return el
        
        return ""