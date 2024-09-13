class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        sols = []
        positions = []
        def get_board(positions):
            board = [['.'] * n for _ in range(n)]
            for i, j in positions:
                board[i][j] = 'Q'
            return [''.join(i) for i in board]
        
        l_r_diag = set() # col - row
        r_l_diag = set() # row + col
        cols = set()
        def backtrack(row):
            if row == n:
                if len(positions) == n:
                    sols.append(get_board(positions))
                return
            
            for col in range(n):
                if (row + col not in r_l_diag and
                    col - row not in l_r_diag and
                    col not in cols):
                    l_r_diag.add(col-row)
                    r_l_diag.add(row+col)
                    cols.add(col)
                    positions.append((row, col))
                    backtrack(row+1)
                    cols.remove(col)
                    l_r_diag.remove(col-row)
                    r_l_diag.remove(row+col)
                    positions.pop()
        backtrack(0)
        return sols
