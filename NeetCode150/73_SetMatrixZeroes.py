class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        M, N = len(matrix), len(matrix[0])

        colzero = False
        for i in range(M):
            if matrix[i][0] == 0:
                colzero = True

        rowzero = False
        for j in range(N):
            if matrix[0][j] == 0:
                rowzero = True

        for i in range(1, M):
            for j in range(1, N):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        for i in range(1, M):
            for j in range(1, N):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        if rowzero:
            for j in range(N):
                matrix[0][j] = 0
        if colzero:
            for i in range(M):
                matrix[i][0] = 0
