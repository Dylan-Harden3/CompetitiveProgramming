class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS = len(matrix), len(matrix[0])

        firstRow, firstCol = False, False

        for i in range(ROWS):
            if matrix[i][0] == 0:
                firstCol = True

        for i in range(COLS):
            if matrix[0][i] == 0:
                firstRow = True

        for i in range(1, ROWS):
            for j in range(1, COLS):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        
        for i in range(1, ROWS):
            for j in range(1, COLS):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if firstCol:
            for i in range(ROWS):
                matrix[i][0] = 0
        
        if firstRow:
            for i in range(COLS):
                matrix[0][i] = 0
                    
