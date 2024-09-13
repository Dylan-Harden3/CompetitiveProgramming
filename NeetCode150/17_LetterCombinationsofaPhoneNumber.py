class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        digit_chars = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        sols = set()
        cur = []
        def backtrack(i):
            if i == len(digits):
                sols.add(''.join(cur))
                return
            
            for c in digit_chars[digits[i]]:
                cur.append(c)
                backtrack(i+1)
                cur.pop()
        
        backtrack(0)
        return sols
