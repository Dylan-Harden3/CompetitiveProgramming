class DetectSquares:

    def __init__(self):
        self.pointsCount = defaultdict(int)
        self.points = []
    def add(self, point: List[int]) -> None:
        self.pointsCount[(point[0], point[1])] += 1
        self.points.append(point)

    def count(self, point: List[int]) -> int:
        x, y = point
        res = 0
        for x1, y1 in self.points:
            if abs(x1-x) != abs(y1-y) or x1 == x or y1 == y:
                continue
            res += self.pointsCount[(x1, y)] * self.pointsCount[(x, y1)]
        return res
