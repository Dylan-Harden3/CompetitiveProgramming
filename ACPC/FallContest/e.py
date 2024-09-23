n, m, k = list(map(int, input().split(' ')))

grid = []

for _ in range(n):
    grid.append(list(input()))

rows = {}
cols = {}

chars = []
for i in range(k):
    chars.append(chr(ord('a') + i).upper())

sol = [['.']*m for _ in range(n)]

for i in range(n):
    c_ix = i % k
    for j in range(m):
        sol[i][j] = chars[c_ix]
        c_ix += 1
        c_ix = c_ix % k

for i in range(n):
    for j in range(m):
        if grid[i][j] == 't':
            grid[i][j] = sol[i][j]

for i in range(n):
    print(''.join(grid[i]))