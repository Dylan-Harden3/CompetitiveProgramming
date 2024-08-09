class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def is_magic(row, col):
            nums = set()
            # 1-9
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    nums.add(grid[row+i][col+j])
            if max(nums) > 9 or len(nums) < 9:
                return False
            # rows
            for i in [-1, 0, 1]:
                if sum(grid[row+i][col-1:col+2]) != 15:
                    return False
            # columns
            for j in [-1, 0, 1]:
                cur = 0
                for i in [-1, 0, 1]:
                    cur += grid[row+i][col+j]
                if cur != 15:
                    return False
            # diagonals
            if grid[row-1][col-1] + grid[row][col] + grid[row+1][col+1] != 15:
                return False
            
            if grid[row-1][col+1] + grid[row][col] + grid[row+1][col-1] != 15:
                return False
            return True
    
        M, N = len(grid), len(grid[0])
        res = 0
        for row in range(1, M-1):
            for col in range(1, N-1):
                res +=  is_magic(row, col)
        return res