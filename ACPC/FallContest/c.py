n = int(input())

arr = list(map(int, input().split(' ')))

l_ptr, r_ptr = 0, n-1
left, right = arr[0], arr[-1]

res = 0

while l_ptr < r_ptr:
    if left == right:
        l_ptr += 1
        r_ptr -= 1
        if l_ptr < r_ptr:
            left = arr[l_ptr]
            right = arr[r_ptr]
    elif left < right:
        left += arr[l_ptr+1]
        l_ptr += 1
        res += 1
    else:
        right += arr[r_ptr-1]
        r_ptr -= 1
        res += 1

print(res)