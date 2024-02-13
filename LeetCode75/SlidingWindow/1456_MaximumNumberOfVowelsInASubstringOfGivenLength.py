class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set()
        vowels.add('a')
        vowels.add('e')
        vowels.add('i')
        vowels.add('o')
        vowels.add('u')

        cur_vowels = 0

        for i in range(k):
            if s[i] in vowels:
                cur_vowels += 1
        
        max_vowels = cur_vowels

        l, r = 0, k

        while r < len(s):
            if s[l] in vowels:
                cur_vowels -= 1
            if s[r] in vowels:
                cur_vowels += 1

            max_vowels = max(max_vowels, cur_vowels)

            l += 1
            r += 1
        
        return max_vowels
