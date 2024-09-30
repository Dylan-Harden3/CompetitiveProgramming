class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [defaultdict(int)]
        i = 0
        while i < len(formula):
            if formula[i] == '(':
                stack.append(defaultdict(int))
            elif formula[i] == ')':
                digit = ""
                while i+1 < len(formula) and formula[i+1].isdigit():
                    digit += formula[i+1]
                    i += 1
                count = int(digit) if digit != "" else 1
                cur_map = stack.pop()
                for k in cur_map:
                    stack[-1][k] += cur_map[k] * count
            else:
                element = formula[i]
                while i+1 < len(formula) and formula[i+1].islower():
                    element += formula[i+1]
                    i += 1
                count = ""
                while i+1 < len(formula) and formula[i+1].isdigit():
                    count += formula[i+1]
                    i += 1
                count = int(count) if count != "" else 1
                stack[-1][element] += count
            i += 1
        
        res = ""
        cur_map = stack.pop()
        for k in sorted(cur_map.keys()):
            res += k
            res += '' if cur_map[k] == 1 else str(cur_map[k])
        return res
