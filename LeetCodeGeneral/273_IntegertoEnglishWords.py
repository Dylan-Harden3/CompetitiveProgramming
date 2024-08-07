class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        ones_map = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
        }

        tens_map = {
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety"
        }

        def get_number_string(n):
            res = []
            hundreds = n // 100
            if hundreds:
                res.append(ones_map[hundreds] + " Hundred")
            tens = n % 100
            if tens >= 20:
                second, first = tens // 10, tens % 10
                res.append(tens_map[second*10])
                if first:
                    res.append(ones_map[first])
            elif tens:
                res.append(ones_map[tens])
            return " ".join(res)

        case = ["", " Thousand", " Million", " Billion"]
        i = 0
        res = []
        while num:
            digits = num % 1000
            s = get_number_string(digits)
            if s:
                res.append(s + case[i])
            i += 1
            num = num // 1000
        res.reverse()
        return " ".join(res)