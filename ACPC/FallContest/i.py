from math import inf, ceil

n, k = list(map(int, input().split(' ')))

arr = list(input())
trees = []
for i in range(n):
    if arr[i] == 'T':
        trees.append(i)

if k > len(trees):
    print(-1)
elif k == 1:
    print(0)
else:
    res = inf
    for i in range(len(trees)):
        if i + (k-1) == len(trees):
            break
        res = min(res, ceil((trees[i+(k-1)]-trees[i])/2))
    print(res)