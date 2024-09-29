class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        for i in range(N // 2):
            for j in range(N-(i*2)-1):
                temp = matrix[i][i+j]
                matrix[i][i+j] = matrix[N-1-i-j][i]
                matrix[N-1-i-j][i] = matrix[N-1-i][N-1-i-j]
                matrix[N-1-i][N-1-i-j] = matrix[i+j][N-1-i]
                matrix[i+j][N-1-i] = temp

