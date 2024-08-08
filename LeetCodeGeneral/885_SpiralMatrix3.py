class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        res = []
        def in_bounds(row, col):
            return min(row, col) >= 0 and row < rows and col < cols

        def search(row, col, direction, count):
            if direction == "Up":
                for _ in range(count):
                    row -= 1
                    if in_bounds(row, col):
                        res.append([row, col])
            elif direction == "Down":
                for _ in range(count):
                    row += 1
                    if in_bounds(row, col):
                        res.append([row, col])
            elif direction == "Left":
                for _ in range(count):
                    col -= 1
                    if in_bounds(row, col):
                        res.append([row, col])
            elif direction == "Right":
                for _ in range(count):
                    col += 1
                    if in_bounds(row, col):
                        res.append([row, col])
            return row, col

        row, col = rStart, cStart
        count = 1
        increment = False
        i = 0
        directions = ["Right", "Down", "Left", "Up"]
        res = [[rStart, cStart]]
        while len(res) < rows * cols:
            row, col = search(row, col, directions[i], count)
            i = (i + 1) % 4
            if increment:
                count += 1
                increment = False
            else:
                increment = True
        return res