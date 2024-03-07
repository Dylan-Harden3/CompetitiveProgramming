class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def distance(x, y):
            return math.sqrt(x**2 +y**2)

        distances = []

        for x, y in points:
            distances.append((distance(x, y), x, y))
        
        heapq.heapify(distances)
        
        res = []
        for _ in range(k):
            cur = heapq.heappop(distances)
            res.append([cur[1], cur[2]])
        return res
