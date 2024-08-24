class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = set()
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in row:
                        return False
                    row.add(board[i][j])

        for i in range(9):
            col = set()
            for j in range(9):
                if board[j][i] != '.':
                    if board[j][i] in col:
                        return False
                    col.add(board[j][i])
        
        digits = set([str(i) for i in range(1, 10)])
        
        for k in range(3):
            g1, g2, g3 = set(), set(), set()
            for i in range(9):
                for j in range(3*k, 3*k + 3):
                    if board[i][j] != '.' and board[i][j] not in digits:
                        return False
                    
                    if board[i][j] != '.':
                        if i < 3:
                            if board[i][j] in g1:
                                return False
                            g1.add(board[i][j])
                        elif i > 5:
                            if board[i][j] in g3:
                                return False
                            g3.add(board[i][j])
                        else:
                            if board[i][j] in g2:
                                return False
                            g2.add(board[i][j])
        return True
