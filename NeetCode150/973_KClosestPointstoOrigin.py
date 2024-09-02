class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []
        for x, y in points:
            heap.append((x**2+y**2, (x, y)))
        heapify(heap)

        res = []
        for _ in range(k):
            __, points = heappop(heap)
            res.append(points)
        return res
