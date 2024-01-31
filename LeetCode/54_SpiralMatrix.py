class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        NUM_ELS = len(matrix) * len(matrix[0])
        
        res = []
        visited = set()
        def search(direction, i, j):
            if direction=='u':
                while i >= 0 and (i, j) not in visited:
                    res.append(matrix[i][j])
                    visited.add((i, j))
                    i -= 1
                i += 1
                j += 1

            elif direction=='d':
                while i < len(matrix) and (i, j) not in visited:
                    res.append(matrix[i][j])
                    visited.add((i, j))
                    i += 1
                i -= 1
                j -= 1
            elif direction=='l':
                while j >= 0 and (i, j) not in visited:
                    res.append(matrix[i][j])
                    visited.add((i, j))
                    j -= 1
                j += 1
                i -= 1
            elif direction=='r':
                while j < len(matrix[0]) and (i, j) not in visited:
                    res.append(matrix[i][j])
                    visited.add((i, j))
                    j += 1
                j -= 1
                i += 1
            return i, j

        dirs = ['r', 'd', 'l', 'u']
        idx = 0
        row, col = 0, 0
        while len(visited) < NUM_ELS:
            row, col = search(dirs[idx], row, col)
            idx = (idx + 1) % 4
        return res
