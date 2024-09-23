n = int(input())
arr = []
for _ in range(n):
    a = input()
    arr.append(1 if a == "ON" else 0)

flips = 0
for i in range(n):
    if flips % 2 == 0 and arr[i] == 0 or flips % 2 == 1 and arr[i] == 1:
        flips += 1
print(flips)