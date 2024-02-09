class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        prefix = [[0] * COLS for _ in range(ROWS)]

        for r in range(ROWS):
            for c in range(COLS):
                above = prefix[r-1][c] if r > 0 else 0
                left = prefix[r][c-1] if c > 0 else 0
                doubled = prefix[r-1][c-1] if min(r, c) > 0 else 0
                prefix[r][c] = matrix[r][c] + above + left - doubled

        res = 0
        for r1 in range(ROWS):
            for r2 in range(r1, ROWS):
                count = defaultdict(int)
                count[0] = 1
                for c in range(COLS):
                    cur_sum = prefix[r2][c] - (prefix[r1-1][c] if r1 > 0 else 0)
                    res += count[cur_sum - target]
                    count[cur_sum] += 1
        return res
