class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occs = [[] for _ in range(len(nums)+1)]

        for n, v in Counter(nums).items():
            occs[v].append(n)

        res = []
        for i in range(len(nums), -1, -1):
            if len(occs[i]):
                for n in occs[i]:
                    res.append(n)
                    if len(res) == k:
                        return res
        return res
