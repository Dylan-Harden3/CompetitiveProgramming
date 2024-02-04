class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counts = Counter(t)
        num_satisfied = 0
        min_window = ""
        cur_counts = defaultdict(int)
        satisfied = defaultdict(bool)
        just_matched = False
        l, r = 0, 0

        while r < len(s):
            if s[r] in t_counts and not just_matched:
                cur_counts[s[r]] += 1
                if cur_counts[s[r]] >= t_counts[s[r]] and not satisfied[s[r]]:
                    num_satisfied += 1
                    satisfied[s[r]] = True
            
            match = True if num_satisfied == len(t_counts) else False
            if match:
                just_matched = True
                if len(min_window) > len(s[l:r+1]) or not min_window:
                    min_window = s[l:r+1]
                if s[l] in cur_counts and s[l] in t_counts:
                    cur_counts[s[l]] -= 1
                    if cur_counts[s[l]] < t_counts[s[l]]:
                        satisfied[s[l]] = False
                        num_satisfied -= 1
                l += 1
                while l < len(s) and s[l] not in t_counts:
                    l += 1
            else:
                r += 1
                just_matched = False
        return min_window

