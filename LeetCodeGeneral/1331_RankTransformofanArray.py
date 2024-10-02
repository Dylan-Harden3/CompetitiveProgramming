class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        cpy = arr.copy()
        ranks = {}
        arr.sort()
        res = []
        prev = -inf
        rank = 0
        for n in arr:
            if n != prev:
                rank += 1
            ranks[n] = rank
            prev = n
        for n in cpy:
            res.append(ranks[n])
        return res
