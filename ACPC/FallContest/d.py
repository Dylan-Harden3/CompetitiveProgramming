from math import ceil
n, k = map(int, input().split(' '))

cur = 1
res = 0

while cur < n:
    if cur > k:
        res += ceil((n-cur) / k)
        break
    else:
        res += 1
        cur += min(cur, k)

print(res)