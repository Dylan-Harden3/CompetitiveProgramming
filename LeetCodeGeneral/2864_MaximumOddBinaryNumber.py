class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        num_ones = Counter(s)['1']
        res = ['0'] * len(s)

        for i in range(num_ones):
            if i == 0:
                res[-1] = '1'
            else:
                res[i-1] = '1'
            
        return ''.join(res)
