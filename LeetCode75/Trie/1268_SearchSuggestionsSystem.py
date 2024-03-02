class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res = []

        l, r = 0, len(products)-1
        for i in range(len(searchWord)):
            while l <= r and (len(products[l]) <= i or products[l][i] != searchWord[i]):
                l += 1
            
            while l <= r and (len(products[r]) <= i or products[r][i] != searchWord[i]):
                r -= 1
            
            cur = []
            for j in range(min(3, r-l+1)):
                cur.append(products[l+j])
            res.append(cur)
        return res
