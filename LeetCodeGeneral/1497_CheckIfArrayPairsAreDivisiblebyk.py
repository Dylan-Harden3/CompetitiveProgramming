class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        bag = defaultdict(int)
        l, r = 0, 0
        pairs = 0
        for i in range(len(arr)):
            if bag[(k - (arr[i] % k)) % k] > 0:
                bag[(k - (arr[i] % k)) % k] -= 1
                pairs += 1
            else:
                bag[arr[i] % k] += 1
        return pairs == len(arr)/2
