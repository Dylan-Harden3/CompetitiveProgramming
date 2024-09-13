class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        M, N = len(board), len(board[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        visit = set()
        
        def search(i, j, word):
            if word == "":
                return True

            if min(i, j) < 0 or i == M or j == N:
                return False
            
            res = False
            if board[i][j] == word[0] and (i, j) not in visit:
                visit.add((i, j))
                for di, dj in dirs:
                    res = res or search(i+di, j+dj, word[1:])
                visit.remove((i, j))
            return res

        for i in range(M):
            for j in range(N):
                if search(i, j, word):
                    return True
        return False
