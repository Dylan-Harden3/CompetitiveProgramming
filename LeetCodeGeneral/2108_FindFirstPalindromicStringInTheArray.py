class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def isPalindrome(s):
            for i in range(len(s)//2):
                if s[i] != s[len(s)-1-i]:
                    return False
            return True
        for s in words:
            if isPalindrome(s):
                return s
        return ""
