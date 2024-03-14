class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        def helper(key):
            flipped, res, l = 0, 0, 0
            for r in range(n):
                if answerKey[r] == key:
                    if flipped < k:
                        flipped += 1
                    else:
                        opposite = 'T' if key == 'F' else 'F'
                        while l < r and answerKey[l] == opposite:
                            l += 1
                        l += 1
                res = max(res, r-l+1)
            return res
        return max(helper('F'), helper('T'))