class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        M, N = len(matrix), len(matrix[0])

        def set_row(row):
            for i in range(N):
                if matrix[row][i] != 0:
                    matrix[row][i] = inf

        def set_col(col):
            for i in range(M):
                if matrix[i][col] != 0:
                    matrix[i][col] = inf
        
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 0:
                    set_row(i)
                    set_col(j)

        for i in range(M):
            for j in range(N):
                if matrix[i][j] == inf:
                    matrix[i][j] = 0
            
