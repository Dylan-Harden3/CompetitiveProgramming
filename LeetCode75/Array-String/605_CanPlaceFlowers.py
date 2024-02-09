class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                return n <= 1
            else:
                return n == 0

        old_count = sum(flowerbed)
        
        for i in range(len(flowerbed)):
            if i == 0:
                if i+1 < len(flowerbed) and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
            elif i == len(flowerbed)-1:
                if i-1 > 0 and flowerbed[i-1] == 0:
                    flowerbed[i] = 1
            else:
                if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1

        return sum(flowerbed) - old_count >= n
