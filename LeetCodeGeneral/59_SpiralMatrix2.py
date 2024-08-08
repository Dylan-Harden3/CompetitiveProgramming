class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[None] * n for _ in range(n)]
    
        def in_bounds(row, col):
            return min(row, col) >= 0 and row < len(res) and col < len(res[0])

        def search(row, col, direction, count):
            if direction == "Up":
                while in_bounds(row, col) and res[row][col] is None:
                    res[row][col] = count
                    count += 1
                    row -= 1
                row += 1
                col += 1
            elif direction == "Down":
                while in_bounds(row, col) and res[row][col] is None:
                    res[row][col] = count
                    count += 1
                    row += 1
                row -= 1
                col -= 1
            elif direction == "Left":
                while in_bounds(row, col) and res[row][col] is None:
                    res[row][col] = count
                    count += 1
                    col -= 1
                col += 1
                row -= 1
            elif direction == "Right":
                while in_bounds(row, col) and res[row][col] is None:
                    res[row][col] = count
                    count += 1
                    col += 1
                col -= 1
                row += 1
            return row, col, count

        row, col = 0, 0
        count = 1
        i = 0
        directions = ["Right", "Down", "Left", "Up"]
        while count <= n*n:
            row, col, count = search(row, col, directions[i], count)
            i = (i + 1) % 4
        return res