class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occs = [[] for _ in range(len(nums) + 1)]
        for num, count in Counter(nums).items():
            occs[count].append(num)

        res = []
        for i in range(len(occs)-1, -1, -1):
            for j in range(len(occs[i])):
                res.append(occs[i][j])
                k -= 1
            if k == 0:
                break
        return res