class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for n1, n2, n3 in zip(arr, arr[1:], arr[2:]):
            if n1 % 2 and n2 % 2 and n3 % 2:
                return True
        return False