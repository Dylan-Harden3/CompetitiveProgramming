class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix)-1

        while l < r:
            for i in range(r-l):
                topLeft = matrix[l][l+i]
                # top left = bottom left
                matrix[l][l+i] = matrix[r-i][l]
                # bottom left = bottom right
                matrix[r-i][l] = matrix[r][r-i]
                # bottom right = top right
                matrix[r][r-i] = matrix[l+i][r]
                # top right = top left
                matrix[l+i][r] = topLeft
            r -= 1
            l += 1
