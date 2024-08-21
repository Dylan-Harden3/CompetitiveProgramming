class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)

        for i in range(N//2):
            # rotate ring i
            for j in range(i, N-1-i):
                prev = matrix[i][j]
                matrix[i][j] = matrix[N-1-j][i]
                matrix[N-1-j][i] = matrix[N-1-i][N-1-j]
                matrix[N-1-i][N-1-j] = matrix[j][N-1-i]
                matrix[j][N-1-i] = prev

