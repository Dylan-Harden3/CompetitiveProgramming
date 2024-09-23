class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        M, N = len(heights), len(heights[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        pacific = set()
        atlantic = set()

        def inBounds(i, j):
            return min(i, j) >= 0 and i < M and j < N

        def search(r, c, ocean):
            if ocean == "p":
                pacific.add((r, c))
            elif ocean == "a":
                atlantic.add((r, c))

            for dr, dc in dirs:
                i, j = r+dr, c+dc
                if inBounds(i, j) and heights[i][j] >= heights[r][c]:
                    if ocean == "p" and (i, j) not in pacific:
                        search(i, j, "p")
                    elif ocean == "a" and (i, j) not in atlantic:
                        search(i, j, "a")

        for i in range(M):
            search(i, 0, "p")
            search(i, N-1, "a")
        
        for i in range(N):
            search(0, i, "p")
            search(M-1, i, "a")

        res = []
        for r, c in atlantic:
            if (r, c) in pacific:
                res.append([r, c])
        return res
