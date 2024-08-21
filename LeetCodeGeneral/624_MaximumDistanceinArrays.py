class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        res = 0
        min_el, max_el = arrays[0][0], arrays[0][-1]

        for arr in arrays[1:]:
            res = max(
                res,
                abs(min_el - arr[-1]),
                abs(arr[0] - max_el)
            )
            min_el = min(min_el, arr[0])
            max_el = max(max_el, arr[-1])
        return res