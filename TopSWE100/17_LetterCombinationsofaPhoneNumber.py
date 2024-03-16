class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "": return []
        digitsToLetters = {}
        digitsToLetters[2] = ['a', 'b', 'c']
        digitsToLetters[3] = ['d', 'e', 'f']
        digitsToLetters[4] = ['g', 'h', 'i']
        digitsToLetters[5] = ['j', 'k', 'l']
        digitsToLetters[6] = ['m', 'n', 'o']
        digitsToLetters[7] = ['p', 'q', 'r', 's']
        digitsToLetters[8] = ['t', 'u', 'v']
        digitsToLetters[9] = ['w', 'x', 'y', 'z']
        res = []
        stack = []
        def backtrack(i):
            if i == len(digits):
                res.append(''.join(stack))
                return
            
            for letter in digitsToLetters[int(digits[i])]:
                stack.append(letter)
                backtrack(i+1)
                stack.pop()
        backtrack(0)
        return res
