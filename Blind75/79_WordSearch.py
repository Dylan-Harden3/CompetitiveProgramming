class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(word, row, col, used):
            if word == "":
                return True

            if (row, col) in used or min(row, col) < 0 or row == ROWS or col == COLS or board[row][col] != word[0]:
                return False
            
            used.add((row, col))
            for d_row, d_col in dirs:
                if dfs(word[1:], row+d_row, col+d_col, used):
                    return True
            used.remove((row, col))
            return False
        
        for i in range(ROWS):
            for j in range(COLS):
                if dfs(word, i, j, set()):
                    return True
        
        return False