class Solution:
    def compress(self, chars: List[str]) -> int:
        i, res = 0, 0

        while i < len(chars):
            cur_letter = chars[i]
            counter = 0

            while i < len(chars) and chars[i] == cur_letter:
                i += 1
                counter += 1

            chars[res] = cur_letter
            res += 1
            if counter > 1:
                for c in str(counter):
                    chars[res] = c
                    res += 1
        return res
