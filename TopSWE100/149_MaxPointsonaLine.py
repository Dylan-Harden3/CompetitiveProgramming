class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
        
        def slope(p1, p2):
            if p2[0] - p1[0] == 0:
                return None
            return (p2[1] - p1[1]) / (p2[0] - p1[0])

        res = 0
        for i in range(len(points)-1):
            p1 = points[i]
            counts = defaultdict(int) # slope -> points
            for j in range(i+1, len(points)):
                p2 = points[j]
                s = slope(p1, p2)
                counts[s] += 1
                res = max(res, counts[s])
        return res+1
