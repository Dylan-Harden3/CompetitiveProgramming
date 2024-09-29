class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        M, N = len(matrix), len(matrix[0])
        res = []
        visit = set()
        r, c = 0, 0
        i = 0
        while len(visit) < M*N:
            if i % 4 == 0: # right
                while c < N and (r, c) not in visit:
                    res.append(matrix[r][c])
                    visit.add((r, c))
                    c += 1
                c -= 1
                r += 1
            elif i % 4 == 1: # down
                while r < M and (r, c) not in visit:
                    res.append(matrix[r][c])
                    visit.add((r, c))
                    r += 1
                r -= 1
                c -= 1
            elif i % 4 == 2: # left
                while c >= 0 and (r, c) not in visit:
                    res.append(matrix[r][c])
                    visit.add((r, c))
                    c -= 1
                c += 1
                r -= 1
            elif i % 4 == 3: # up
                while r >= 0 and (r, c) not in visit:
                    res.append(matrix[r][c])
                    visit.add((r, c))
                    r -= 1
                r += 1
                c += 1
            i += 1
        return res
