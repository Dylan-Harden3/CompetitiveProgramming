class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        RES_LEN = len(matrix) * len(matrix[0])
        res = []
        directions = ["Right", "Down", "Left", "Up"]
        def in_bounds(row, col):
            return min(row, col) >= 0 and row < len(matrix) and col < len(matrix[0])

        def search(row, col, direction):
            if direction == "Up":
                while in_bounds(row, col) and matrix[row][col] != -999:
                    res.append(matrix[row][col])
                    matrix[row][col] = -999
                    row -= 1
                row += 1
                col += 1
            elif direction == "Down":
                while in_bounds(row, col) and matrix[row][col] != -999:
                    res.append(matrix[row][col])
                    matrix[row][col] = -999
                    row += 1
                row -= 1
                col -= 1
            elif direction == "Left":
                while in_bounds(row, col) and matrix[row][col] != -999:
                    res.append(matrix[row][col])
                    matrix[row][col] = -999
                    col -= 1
                col += 1
                row -= 1
            elif direction == "Right":
                while in_bounds(row, col) and matrix[row][col] != -999:
                    res.append(matrix[row][col])
                    matrix[row][col] = -999
                    col += 1
                col -= 1
                row += 1
            return row, col
        i = 0
        row, col = 0, 0
        while len(res) < RES_LEN:
            row, col = search(row, col, directions[i])
            i = (i+1) % 4
        return res