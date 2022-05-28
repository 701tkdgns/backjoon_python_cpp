n = int(input())
lst = list(map(int, input().split()))
x = int(input())
lst.sort()
res = 0
idx_l, idx_r = 0, n-1
while idx_l < idx_r:
    if lst[idx_l] + lst[idx_r] == x:
        res += 1
        idx_l += 1
        idx_r -= 1
    elif lst[idx_l] + lst[idx_r] < x:
        idx_l += 1
    else:
        idx_r -= 1
print(res)
